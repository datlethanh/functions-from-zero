#!/usr/bin/env python3
from mylib.calc import add, subtract, multiply, divide, power
import click

@click.group()
def cli():
    """A simple calculator CLI."""
    
@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers.
    
    Usage: calcCLI.py add <a> <b>
    Example: calcCLI.py add 2 3
    """
    #use colored output to print the result in green
    click.secho(f"{a} + {b} = {add(a, b)}", fg="green")

@cli.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    """Subtract two numbers.
    
    Usage: calcCLI.py subtract <a> <b>
    Example: calcCLI.py subtract 5 2
    """
    click.secho(f"{a} - {b} = {subtract(a, b)}", fg="green")  

@cli.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    """Multiply two numbers.
    
    Usage: calcCLI.py multiply <a> <b>
    Example: calcCLI.py multiply 3 4
    """
    click.secho(f"{a} * {b} = {multiply(a, b)}", fg="green") 

@cli.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    """Divide two numbers.
    
    Usage: calcCLI.py divide <a> <b>
    Example: calcCLI.py divide 10 2
    """
    try:
        result = divide(a, b)
        click.secho(f"{a} / {b} = {result}", fg="green")
    except ValueError as e:
        click.secho(str(e), fg="red")  

@cli.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_command(x, y):
    """Calculate x raised to the power of y.
    
    Usage: calcCLI.py power <x> <y>
    Example: calcCLI.py power 2 3
    """
    click.secho(f"{x} ^ {y} = {power(x, y)}", fg="green")

if __name__ == "__main__":
    cli()
    