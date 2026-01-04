"""Input validation functions for calculator."""

from decimal import Decimal, InvalidOperation


def validate_decimal(value: str) -> Decimal:
    """
    Validate and convert string to Decimal.

    Args:
        value: String representation of a number

    Returns:
        Decimal representation of the value

    Raises:
        ValueError: If value is not a valid decimal format
    """
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid number format")


def validate_division_by_zero(divisor: Decimal) -> None:
    """
    Validate that divisor is not zero.

    Args:
        divisor: The divisor in a division operation

    Raises:
        ValueError: If divisor is zero
    """
    if divisor == Decimal("0"):
        raise ValueError("Cannot divide by zero")
