"""Data models for calculator state and calculations."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, Optional

# Type alias for the four supported arithmetic operations
Operator = Literal["add", "subtract", "multiply", "divide"]


@dataclass
class CalculatorState:
    """Manages calculator state during user interactions."""

    current_value: str = "0"
    previous_value: str = ""
    operator: Optional[Operator] = None
    should_reset_display: bool = False
    error: Optional[str] = None

    def reset(self) -> None:
        """Reset calculator to initial state (C button)."""
        self.current_value = "0"
        self.previous_value = ""
        self.operator = None
        self.should_reset_display = False
        self.error = None

    def set_error(self, message: str) -> None:
        """Set error state."""
        self.error = message
        self.current_value = f"Error: {message}"

    def clear_error(self) -> None:
        """Clear error state."""
        self.error = None

    def has_error(self) -> bool:
        """Check if calculator is in error state."""
        return self.error is not None


@dataclass
class Calculation:
    """Represents a single arithmetic calculation."""

    operand1: Decimal
    operand2: Decimal
    operator: Operator
    result: Optional[Decimal] = None

    @classmethod
    def from_state(cls, state: CalculatorState) -> "Calculation":
        """Create Calculation from CalculatorState."""
        from .validators import validate_decimal

        operand1 = validate_decimal(state.previous_value)
        operand2 = validate_decimal(state.current_value)

        return cls(
            operand1=operand1,
            operand2=operand2,
            operator=state.operator,  # type: ignore[arg-type]
            result=None,
        )

    def execute(self) -> Decimal:
        """Execute the calculation and store result."""
        from .operations import add, divide, multiply, subtract

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }

        self.result = operations[self.operator](self.operand1, self.operand2)
        return self.result
