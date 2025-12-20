import pytest
from click.testing import CliRunner
from calcCLI import cli


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_add_command(runner):
    """Test the add command."""
    result = runner.invoke(cli, ["add", "5", "3"])
    assert result.exit_code == 0
    assert "5.0 + 3.0 = 8.0" in result.output


def test_add_command_with_floats(runner):
    """Test the add command with floating point numbers."""
    result = runner.invoke(cli, ["add", "2.5", "3.5"])
    assert result.exit_code == 0
    assert "2.5 + 3.5 = 6.0" in result.output


def test_subtract_command(runner):
    """Test the subtract command."""
    result = runner.invoke(cli, ["subtract", "10", "4"])
    assert result.exit_code == 0
    assert "10.0 - 4.0 = 6.0" in result.output


def test_multiply_command(runner):
    """Test the multiply command."""
    result = runner.invoke(cli, ["multiply", "6", "7"])
    assert result.exit_code == 0
    assert "6.0 * 7.0 = 42.0" in result.output


def test_divide_command(runner):
    """Test the divide command."""
    result = runner.invoke(cli, ["divide", "20", "5"])
    assert result.exit_code == 0
    assert "20.0 / 5.0 = 4.0" in result.output


def test_divide_by_zero(runner):
    """Test the divide command with division by zero."""
    result = runner.invoke(cli, ["divide", "10", "0"])
    assert result.exit_code == 0
    # The command handles the exception and prints an error message
    assert "Cannot divide by zero" in result.output


def test_power_command(runner):
    """Test the power command."""
    result = runner.invoke(cli, ["power", "2", "8"])
    assert result.exit_code == 0
    assert "2.0 ^ 8.0 = 256.0" in result.output


def test_missing_arguments(runner):
    """Test commands with missing arguments."""
    commands = ["add", "subtract", "multiply", "divide", "power"]
    for command in commands:
        result = runner.invoke(cli, [command, "5"])
        assert result.exit_code == 2  # click exits with 2 for usage errors
        assert "Error: Missing argument" in result.output


def test_invalid_arguments(runner):
    """Test commands with invalid (non-float) arguments."""
    commands = ["add", "subtract", "multiply", "divide", "power"]
    for command in commands:
        result = runner.invoke(cli, [command, "a", "b"])
        assert result.exit_code == 2
        assert "Invalid value for" in result.output


def test_too_many_arguments(runner):
    """Test commands with too many arguments."""
    result = runner.invoke(cli, ["add", "1", "2", "3"])
    assert result.exit_code == 2
    assert "Got unexpected extra argument" in result.output


def test_unknown_option(runner):
    """Test commands with unknown options."""
    result = runner.invoke(cli, ["add", "1", "2", "--unknown"])
    assert result.exit_code == 2
    assert "No such option" in result.output


def test_main_cli_help(runner):
    """Test the main CLI help message."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage: cli [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "A simple calculator CLI." in result.output
    assert "add" in result.output
    assert "divide" in result.output
