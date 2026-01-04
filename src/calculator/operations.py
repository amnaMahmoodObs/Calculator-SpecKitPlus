"""Pure arithmetic operations for calculator."""

from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal:
    """Add two decimal numbers."""
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtract b from a."""
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiply two decimal numbers."""
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divide a by b."""
    return a / b
