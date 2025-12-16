from hello import hello


def test_hello_with_name():
    """Test hello function with a typical name."""
    assert hello("World") == "Hello, World!"


def test_hello_with_another_name():
    """Test hello function with a different name."""
    assert hello("Bob") == "Hello, Bob!"


def test_hello_with_empty_string():
    """Test hello function with an empty string."""
    assert hello("") == "Hello, !"
