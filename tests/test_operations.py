"""Tests for calculator arithmetic operations (TDD - written FIRST)."""

import pytest
from decimal import Decimal
from src.calculator.operations import add, subtract, multiply, divide


class TestBasicArithmetic:
    """Tests for User Story 1: Basic Arithmetic Operations."""

    def test_add(self) -> None:
        """Test addition with positive numbers."""
        result = add(Decimal("5"), Decimal("3"))
        assert result == Decimal("8")

        result = add(Decimal("10.5"), Decimal("2.3"))
        assert result == Decimal("12.8")

    def test_subtract(self) -> None:
        """Test subtraction."""
        result = subtract(Decimal("10"), Decimal("4"))
        assert result == Decimal("6")

        result = subtract(Decimal("15.5"), Decimal("3.2"))
        assert result == Decimal("12.3")

    def test_multiply(self) -> None:
        """Test multiplication."""
        result = multiply(Decimal("7"), Decimal("6"))
        assert result == Decimal("42")

        result = multiply(Decimal("2.5"), Decimal("4"))
        assert result == Decimal("10")

    def test_divide(self) -> None:
        """Test division (non-zero divisor)."""
        result = divide(Decimal("20"), Decimal("4"))
        assert result == Decimal("5")

        result = divide(Decimal("15"), Decimal("3"))
        assert result == Decimal("5")

    def test_operations_with_integers(self) -> None:
        """Test integer arithmetic."""
        assert add(Decimal("100"), Decimal("50")) == Decimal("150")
        assert subtract(Decimal("100"), Decimal("50")) == Decimal("50")
        assert multiply(Decimal("10"), Decimal("5")) == Decimal("50")
        assert divide(Decimal("100"), Decimal("10")) == Decimal("10")


class TestDecimalPrecision:
    """Tests for User Story 2: Decimal Number Support."""

    def test_decimal_addition_precision(self) -> None:
        """Test 0.1 + 0.2 = 0.3 (no floating-point errors)."""
        result = add(Decimal("0.1"), Decimal("0.2"))
        assert result == Decimal("0.3")

    def test_decimal_multiplication(self) -> None:
        """Test 5.5 * 2.2 = 12.1."""
        result = multiply(Decimal("5.5"), Decimal("2.2"))
        assert result == Decimal("12.1")

    def test_decimal_division_exact(self) -> None:
        """Test 10.5 / 2.1 = 5."""
        result = divide(Decimal("10.5"), Decimal("2.1"))
        assert result == Decimal("5")

    def test_decimal_division_repeating(self) -> None:
        """Test 10 / 3 with precision."""
        result = divide(Decimal("10"), Decimal("3"))
        # Should have high precision, not just 3.333...
        assert str(result).startswith("3.3333333")

    def test_decimal_normalization(self) -> None:
        """Ensure trailing zeros removed."""
        result = add(Decimal("5.50"), Decimal("0"))
        normalized = result.normalize()
        assert str(normalized) == "5.5"


class TestNegativeNumbers:
    """Tests for User Story 3: Error Handling - Negative Numbers."""

    def test_add_with_negatives(self) -> None:
        """Test -5 + 3 = -2."""
        result = add(Decimal("-5"), Decimal("3"))
        assert result == Decimal("-2")

    def test_multiply_negatives(self) -> None:
        """Test -10 * -2 = 20."""
        result = multiply(Decimal("-10"), Decimal("-2"))
        assert result == Decimal("20")
