import argparse
import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def main(n_estimators, max_depth):
    print(f"Running experiment with n_estimators={n_estimators}, max_depth={max_depth}")
    # Fetch Fashion MNIST dataset
    print("Fetching Fashion MNIST dataset...")
    # as_frame=False returns numpy arrays, parser='auto' suppresses warnings
    X, y = fetch_openml('Fashion-MNIST', version=1, return_X_y=True, as_frame=False, parser='auto')
    
    # Use a subset for faster demonstration
    X = X[:2000]
    y = y[:2000]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Enable auto-logging
    mlflow.sklearn.autolog()

    with mlflow.start_run():
        clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        clf.fit(X_train, y_train)
        
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        print(f"Accuracy: {accuracy}")
        mlflow.log_metric("test_accuracy", accuracy)

        # Create and log confusion matrix plot
        print("Creating and logging confusion matrix plot...")
        cm = confusion_matrix(y_test, predictions)
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Blues')
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title('Confusion Matrix')
        
        # Save plot and log it as an artifact in a 'plots' directory
        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png", "plots")
        plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=200)
    parser.add_argument("--max_depth", type=int, default=20)
    args = parser.parse_args()
    
    main(args.n_estimators, args.max_depth)
