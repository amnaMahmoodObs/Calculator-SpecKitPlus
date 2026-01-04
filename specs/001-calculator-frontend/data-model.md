# Data Model: Pastel Calculator with Tkinter GUI

**Feature**: 001-calculator-frontend
**Date**: 2026-01-04 (Revised for tkinter)
**Phase**: 1 - Data Modeling

## Overview

This calculator is a stateless desktop application with no data persistence. All entities represent internal state and calculation models.

## Core Entities

### 1. Operator (Type Alias)

**Purpose**: Represents the four supported arithmetic operations

**Type**: Literal type alias (string-based for clarity)

**Values**:
- `"add"` - Addition operation
- `"subtract"` - Subtraction operation
- `"multiply"` - Multiplication operation
- `"divide"` - Division operation

**Validation Rules**:
- MUST be one of the four exact string values (case-sensitive)
- No custom operators allowed
- Enforced by type hints

**Python Implementation**:
```python
from typing import Literal

Operator = Literal["add", "subtract", "multiply", "divide"]
```

**Usage**:
```python
def calculate(op: Operator, a: Decimal, b: Decimal) -> Decimal:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    return operations[op](a, b)
```

---

### 2. CalculatorState

**Purpose**: Manages the internal state of the calculator during user interactions

**Attributes**:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| current_value | str | "0" | Currently displayed value (number being entered) |
| previous_value | str | "" | Previous operand (stored when operator clicked) |
| operator | Operator \| None | None | Selected arithmetic operation |
| should_reset_display | bool | False | Flag to clear display on next digit entry |
| error | str \| None | None | Error message (if any), None means no error |

**State Transitions**:

```
State 1: Initial
  current_value="0", previous_value="", operator=None

State 2: Entering first number
  User presses "5"
  → current_value="5"

State 3: Operator selected
  User presses "+"
  → previous_value="5", operator="add", should_reset_display=True

State 4: Entering second number
  User presses "3"
  → current_value="3" (display was reset due to should_reset_display)

State 5: Calculate
  User presses "="
  → Compute: Decimal("5") + Decimal("3") = Decimal("8")
  → current_value="8", previous_value="", operator=None

State 6: Error
  User enters "5 / 0" and presses "="
  → error="Cannot divide by zero", current_value shows error
```

**Validation Rules**:
- current_value MUST be parseable to Decimal when calculating
- operator MUST be one of the four Operator values or None
- error being set triggers error display in GUI

**Python Model**:
```python
from dataclasses import dataclass
from typing import Optional, Literal

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
```

---

### 3. Calculation

**Purpose**: Represents a single arithmetic operation with its operands and result

**Attributes**:

| Field | Type | Description |
|-------|------|-------------|
| operand1 | Decimal | First operand |
| operand2 | Decimal | Second operand |
| operator | Operator | Operation to perform |
| result | Decimal | Calculated result |

**Lifecycle**:
1. Parse current_value and previous_value from CalculatorState
2. Convert strings to Decimal
3. Validate (division by zero check if applicable)
4. Execute operation
5. Return result as Decimal
6. Convert result to string for display

**Python Model**:
```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Calculation:
    """Represents a single arithmetic calculation."""

    operand1: Decimal
    operand2: Decimal
    operator: Operator
    result: Decimal | None = None

    @classmethod
    def from_state(cls, state: CalculatorState) -> 'Calculation':
        """Create Calculation from CalculatorState."""
        from .validators import validate_decimal

        operand1 = validate_decimal(state.previous_value)
        operand2 = validate_decimal(state.current_value)

        return cls(
            operand1=operand1,
            operand2=operand2,
            operator=state.operator,  # type: ignore (checked before calling)
            result=None
        )

    def execute(self) -> Decimal:
        """Execute the calculation and store result."""
        from .operations import add, subtract, multiply, divide

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }

        self.result = operations[self.operator](self.operand1, self.operand2)
        return self.result
```

**Usage Example**:
```python
# In GUI when user presses "="
state = CalculatorState(
    previous_value="5.5",
    current_value="2.2",
    operator="multiply"
)

calculation = Calculation.from_state(state)
result = calculation.execute()  # Decimal('12.1')

state.current_value = str(result.normalize())  # "12.1"
state.operator = None
state.previous_value = ""
```

---

## Entity Relationships

```
┌─────────────────────┐
│  CalculatorState    │ (Managed by GUI)
│  - current_value    │
│  - previous_value   │
│  - operator         │
│  - should_reset     │
│  - error            │
└──────────┬──────────┘
           │
           │ User presses "="
           │
           ▼
┌─────────────────────┐
│    Calculation      │ (Created on demand)
│  - operand1: Decimal│ ← parse previous_value
│  - operand2: Decimal│ ← parse current_value
│  - operator         │ ← from state
│  - result: Decimal  │
└──────────┬──────────┘
           │
           │ execute()
           │
           ▼
┌─────────────────────┐
│  Update State       │
│  current_value =    │
│    str(result)      │
│  operator = None    │
│  previous_value = ""│
└─────────────────────┘
```

---

## State Flow Diagram

### Happy Path: 5 + 3 = 8

```
Initial State:
  current_value="0"
  previous_value=""
  operator=None

User presses "5":
  current_value="5"

User presses "+":
  previous_value="5"
  current_value="5" (not yet reset)
  operator="add"
  should_reset_display=True

User presses "3":
  Check should_reset_display → True
  current_value="3" (reset display)
  should_reset_display=False

User presses "=":
  Create Calculation:
    operand1=Decimal("5")
    operand2=Decimal("3")
    operator="add"
  Execute: 5 + 3 = 8
  Update State:
    current_value="8"
    previous_value=""
    operator=None
```

### Error Path: 10 / 0

```
Initial State:
  current_value="0"
  ...

User enters "10", presses "/", enters "0", presses "=":

Create Calculation:
  operand1=Decimal("10")
  operand2=Decimal("0")
  operator="divide"

Validate division by zero:
  divisor == 0 → raise ValueError("Cannot divide by zero")

Catch ValueError in GUI:
  state.set_error("Cannot divide by zero")
  current_value="Error: Cannot divide by zero"
  error="Cannot divide by zero"

User presses "C" (Clear):
  state.reset()
  current_value="0"
  error=None
```

---

## Validation Summary

| Validation | When | Enforced By | Error Handling |
|------------|------|-------------|----------------|
| Decimal format | On "=" press | validate_decimal() in validators.py | ValueError → GUI shows error |
| Division by zero | On "=" press (if operator is divide) | validate_division_by_zero() | ValueError → GUI shows error |
| Operator validity | On operator button click | Type hint (Operator literal) | mypy compile-time check |
| State consistency | Throughout | Dataclass with defaults | Type-safe state transitions |

---

## GUI Integration

### Display Updates

```python
# gui.py
class CalculatorGUI:
    def __init__(self, root: tk.Tk):
        self.state = CalculatorState()
        self.display = tk.Entry(...)

    def update_display(self):
        """Sync display with state."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.state.current_value)

        # Change color if error
        if self.state.has_error():
            self.display.config(fg="red")
        else:
            self.display.config(fg="black")

    def on_number_click(self, digit: str):
        """Handle number button clicks."""
        if self.state.should_reset_display:
            self.state.current_value = digit
            self.state.should_reset_display = False
        elif self.state.current_value == "0":
            self.state.current_value = digit
        else:
            self.state.current_value += digit

        self.update_display()

    def on_operator_click(self, operator: Operator):
        """Handle operator button clicks."""
        if self.state.operator is not None:
            # Chain calculations: 5 + 3 + (presses +)
            # First calculate 5 + 3, then set new operator
            self.on_equals_click()

        self.state.previous_value = self.state.current_value
        self.state.operator = operator
        self.state.should_reset_display = True

    def on_equals_click(self):
        """Handle equals button click."""
        if self.state.operator is None:
            return  # Nothing to calculate

        try:
            calculation = Calculation.from_state(self.state)

            # Validate division by zero
            if self.state.operator == "divide":
                validate_division_by_zero(calculation.operand2)

            result = calculation.execute()

            # Update state with result
            self.state.current_value = str(result.normalize())
            self.state.previous_value = ""
            self.state.operator = None
            self.state.clear_error()

        except ValueError as e:
            self.state.set_error(str(e))

        self.update_display()

    def on_clear_click(self):
        """Handle clear button click."""
        self.state.reset()
        self.update_display()
```

---

## Precision Configuration

**Decimal Context**:
```python
# main.py
from decimal import getcontext

def main():
    # Set decimal precision at app startup
    getcontext().prec = 28  # Python default, 28 significant digits

    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

**Precision Details**:
- **28 significant digits**: Sufficient for calculator use
- **No rounding mode override**: Uses default ROUND_HALF_EVEN
- **Normalize results**: Remove trailing zeros (`Decimal('5.50').normalize()` → `Decimal('5.5')`)

**Example**:
- Input: "0.1" + "0.2"
- Internal: `Decimal('0.1') + Decimal('0.2')` = `Decimal('0.3')`
- Display: "0.3" (exact, no floating-point error)

---

## Testing Approach

### Unit Tests (business logic)

```python
# tests/test_models.py
def test_calculator_state_reset():
    state = CalculatorState(
        current_value="42",
        previous_value="10",
        operator="add"
    )
    state.reset()

    assert state.current_value == "0"
    assert state.previous_value == ""
    assert state.operator is None

def test_calculation_from_state():
    state = CalculatorState(
        previous_value="5.5",
        current_value="2.2",
        operator="multiply"
    )

    calc = Calculation.from_state(state)

    assert calc.operand1 == Decimal("5.5")
    assert calc.operand2 == Decimal("2.2")
    assert calc.operator == "multiply"

def test_calculation_execute():
    calc = Calculation(
        operand1=Decimal("10"),
        operand2=Decimal("3"),
        operator="divide"
    )

    result = calc.execute()

    assert result == Decimal("10") / Decimal("3")
    assert calc.result == result
```

### Manual GUI Tests

1. **State display sync**: Enter "5", verify display shows "5"
2. **Operator flow**: Enter "5", press "+", enter "3", press "=", verify "8"
3. **Error display**: Enter "10", press "/", enter "0", press "=", verify red error text
4. **Clear function**: After error, press "C", verify display resets to "0" with black text
5. **Chained operations**: Enter "5", press "+", enter "3", press "+", verify shows "8", then enter "2", press "=", verify "10"

---

## Next Steps

1. Implement operations.py with pure arithmetic functions
2. Implement validators.py with decimal parsing and error checking
3. Implement models.py with CalculatorState and Calculation dataclasses
4. Implement gui.py with tkinter widgets and event handlers
5. Implement main.py with decimal precision setup and app launch
