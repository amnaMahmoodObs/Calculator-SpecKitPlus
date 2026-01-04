"""Tests for calculator models (TDD - written FIRST)."""

import pytest
from decimal import Decimal
from src.calculator.models import CalculatorState, Calculation


class TestCalculatorState:
    """Tests for CalculatorState dataclass."""

    def test_initial_state(self) -> None:
        """Test default initial state."""
        state = CalculatorState()
        assert state.current_value == "0"
        assert state.previous_value == ""
        assert state.operator is None
        assert state.should_reset_display is False
        assert state.error is None

    def test_reset(self) -> None:
        """Test reset() method."""
        state = CalculatorState(
            current_value="42",
            previous_value="10",
            operator="add",
            should_reset_display=True,
            error="Some error",
        )
        state.reset()

        assert state.current_value == "0"
        assert state.previous_value == ""
        assert state.operator is None
        assert state.should_reset_display is False
        assert state.error is None

    def test_set_error(self) -> None:
        """Test set_error() method."""
        state = CalculatorState()
        state.set_error("Cannot divide by zero")

        assert state.error == "Cannot divide by zero"
        assert state.current_value == "Error: Cannot divide by zero"

    def test_clear_error(self) -> None:
        """Test clear_error() method."""
        state = CalculatorState()
        state.set_error("Some error")
        state.clear_error()

        assert state.error is None
        # Note: current_value remains as "Error: ..." until reset or new value

    def test_has_error(self) -> None:
        """Test has_error() method."""
        state = CalculatorState()
        assert state.has_error() is False

        state.set_error("Error message")
        assert state.has_error() is True

        state.clear_error()
        assert state.has_error() is False


class TestCalculation:
    """Tests for Calculation dataclass."""

    def test_from_state(self) -> None:
        """Test Calculation.from_state() factory method."""
        state = CalculatorState(
            previous_value="5.5", current_value="2.2", operator="multiply"
        )

        calc = Calculation.from_state(state)

        assert calc.operand1 == Decimal("5.5")
        assert calc.operand2 == Decimal("2.2")
        assert calc.operator == "multiply"
        assert calc.result is None

    def test_execute_addition(self) -> None:
        """Test execute() for addition."""
        calc = Calculation(
            operand1=Decimal("5"), operand2=Decimal("3"), operator="add"
        )

        result = calc.execute()

        assert result == Decimal("8")
        assert calc.result == Decimal("8")

    def test_execute_subtraction(self) -> None:
        """Test execute() for subtraction."""
        calc = Calculation(
            operand1=Decimal("10"), operand2=Decimal("4"), operator="subtract"
        )

        result = calc.execute()

        assert result == Decimal("6")
        assert calc.result == Decimal("6")

    def test_execute_multiplication(self) -> None:
        """Test execute() for multiplication."""
        calc = Calculation(
            operand1=Decimal("7"), operand2=Decimal("6"), operator="multiply"
        )

        result = calc.execute()

        assert result == Decimal("42")
        assert calc.result == Decimal("42")

    def test_execute_division(self) -> None:
        """Test execute() for division."""
        calc = Calculation(
            operand1=Decimal("20"), operand2=Decimal("4"), operator="divide"
        )

        result = calc.execute()

        assert result == Decimal("5")
        assert calc.result == Decimal("5")
