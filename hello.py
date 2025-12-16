# create a hello function that uses an f-string to return the string "Hello, {name}!" where name is a parameter passed to the function
def hello(name):
    return f"Hello, {name}!"


# Example usage:
if __name__ == "__main__":
    print(hello("Alice"))  # Output: Hello, Alice!
