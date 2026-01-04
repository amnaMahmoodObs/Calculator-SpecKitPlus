"""Tests for input validation (TDD - written FIRST)."""

import pytest
from decimal import Decimal
from src.calculator.validators import validate_decimal, validate_division_by_zero


class TestValidateDecimal:
    """Tests for User Story 3: Error Handling - Decimal Validation."""

    def test_validate_decimal_valid(self) -> None:
        """Test valid decimal strings."""
        assert validate_decimal("5") == Decimal("5")
        assert validate_decimal("3.14") == Decimal("3.14")
        assert validate_decimal("0.1") == Decimal("0.1")
        assert validate_decimal("-10") == Decimal("-10")

    def test_validate_decimal_invalid(self) -> None:
        """Test invalid input raises ValueError."""
        with pytest.raises(ValueError, match="Invalid number format"):
            validate_decimal("abc")

        with pytest.raises(ValueError, match="Invalid number format"):
            validate_decimal("12.34.56")

    def test_validate_decimal_empty(self) -> None:
        """Test empty string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid number format"):
            validate_decimal("")


class TestValidateDivisionByZero:
    """Tests for User Story 3: Error Handling - Division by Zero."""

    def test_validate_division_by_zero(self) -> None:
        """Test divisor=0 raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            validate_division_by_zero(Decimal("0"))

    def test_validate_division_by_nonzero(self) -> None:
        """Test divisor!=0 passes validation."""
        # Should not raise any exception
        validate_division_by_zero(Decimal("5"))
        validate_division_by_zero(Decimal("0.1"))
        validate_division_by_zero(Decimal("-3"))
