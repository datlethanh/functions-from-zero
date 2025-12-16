import pytest
from mylib.calc import add, subtract, multiply, divide, power


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(5, 5) == 0


def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(5, 0) == 0


def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(1, 0)


def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3