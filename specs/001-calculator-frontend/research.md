# Research: Pastel Calculator with Tkinter GUI

**Feature**: 001-calculator-frontend
**Date**: 2026-01-04 (Revised for tkinter)
**Phase**: 0 - Technology Research and Decision Making

## Research Questions and Decisions

### 1. GUI Framework Selection

**Question**: Which Python GUI framework best supports type safety, decimal precision, cross-platform compatibility, and simple calculator development?

**Options Evaluated**:
1. **tkinter** - Standard library, cross-platform, simple, no external deps
2. **PyQt/PySide** - Powerful but complex, large dependency, licensing concerns
3. **Kivy** - Mobile-focused, overkill for simple calculator
4. **wxPython** - Cross-platform but requires installation

**Decision**: tkinter

**Rationale**:
- **No external dependencies**: Part of Python standard library (aligns with constitution principle V - simplicity)
- **Cross-platform**: Works on Windows, macOS, Linux without modification
- **Simple API**: Straightforward for calculator UI (buttons, display, event handlers)
- **Type safety compatible**: Works with mypy type hints
- **Lightweight**: Minimal resource usage, fast startup
- **Mature and stable**: Been in Python stdlib since 1.4
- **Suitable for pastel colors**: Full color customization via tkinter.ttk or tk.Button config

**Alternatives Considered**:
- PyQt/PySide: Rejected due to external dependency, licensing complexity, over-engineered for calculator
- Kivy: Rejected as mobile-focused, unnecessary complexity
- wxPython: Rejected as requires pip install, tkinter already in stdlib

---

### 2. Application Architecture

**Question**: How to structure tkinter application to maintain separation of concerns and testability?

**Options Evaluated**:
1. **MVC Pattern** - Model-View-Controller with separate files
2. **Single File** - All code in one file (simple but untestable)
3. **Business Logic Separation** - operations/validators separate from GUI

**Decision**: Business Logic Separation (lightweight MVC)

**Rationale**:
- **Testability**: Pure functions (operations, validators) can be unit tested without GUI
- **Constitution compliance**: Single responsibility principle (Principle V)
- **Type safety**: Separate modules enable strict mypy checking
- **Maintainability**: GUI changes don't affect business logic

**File Structure**:
```python
# operations.py - Pure functions (testable)
def add(a: Decimal, b: Decimal) -> Decimal: ...

# validators.py - Input validation (testable)
def validate_decimal(value: str) -> Decimal: ...

# models.py - Data classes (testable)
@dataclass
class CalculatorState: ...

# gui.py - Tkinter widgets (manual testing)
class CalculatorGUI:
    def __init__(self, root: tk.Tk): ...
    def on_button_click(self, value: str): ...

# main.py - Entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
```

**Alternatives Considered**:
- Full MVC with Controller: Rejected as over-engineering for simple calculator
- Single file: Rejected as untestable, violates constitution

---

### 3. Decimal Precision Implementation

**Question**: How to implement decimal.Decimal in tkinter calculator?

**Decision**: Backend decimal.Decimal with string display/input

**Rationale**:
- Python decimal.Decimal provides arbitrary precision (constitution principle VI)
- Display shows string representation: `str(Decimal('0.1') + Decimal('0.2'))` → `"0.3"`
- Input parsed from Entry widget as string: `Decimal(entry.get())`
- Avoids 0.1 + 0.2 = 0.30000000000000004 issue entirely
- Set getcontext().prec = 28 (Python default) for sufficient precision

**Implementation Details**:
```python
# main.py or config module
from decimal import Decimal, getcontext
getcontext().prec = 28  # Set at app startup

# operations.py
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

# gui.py
def calculate(self):
    operand1 = Decimal(self.current_value)
    operand2 = Decimal(self.previous_value)
    result = operations.add(operand1, operand2)
    self.display.delete(0, tk.END)
    self.display.insert(0, str(result))
```

**Alternatives Considered**:
- Float: Rejected due to precision errors (violates constitution principle VI)
- External decimal library: Rejected as stdlib Decimal sufficient

---

### 4. Error Handling Strategy

**Question**: How to display errors in tkinter GUI?

**Options Evaluated**:
1. **MessageBox popups** - Modal dialogs (disruptive)
2. **Display field errors** - Show error in calculator display (inline)
3. **Status label** - Separate label for errors (extra widget)

**Decision**: Display field errors with color indication

**Rationale**:
- **Non-disruptive**: User sees error without modal dialog interruption
- **Clear visual feedback**: Red text or background indicates error
- **Simple implementation**: Just update display text and color
- **Follows calculator conventions**: Real calculators show "Error" in display
- **Constitution principle II**: Error handling first (validate before calc)

**Error Display Pattern**:
```python
def show_error(self, message: str):
    self.display.delete(0, tk.END)
    self.display.insert(0, f"Error: {message}")
    self.display.config(fg="red")  # Red text for errors

def clear_error(self):
    self.display.config(fg="black")  # Reset to normal
```

**Error Types**:
- Division by zero: "Error: Cannot divide by zero"
- Invalid input: "Error: Invalid input"
- Overflow: "Error: Number too large"

**Alternatives Considered**:
- MessageBox: Rejected as disruptive (requires clicking OK)
- Status label: Rejected as adds UI complexity

---

### 5. Validation Strategy

**Question**: When and where should validation occur in tkinter app?

**Decision**: Validate on calculation trigger (equals button or Enter key)

**Rationale**:
- **User-friendly**: Allow typing anything, validate when computing
- **Constitution principle III**: Validate all input before computation
- **Clear error feedback**: Errors shown in display when user attempts calculation
- **Type safety**: validators.py functions return Decimal or raise ValueError

**Validation Flow**:
```python
# validators.py
def validate_decimal(value: str) -> Decimal:
    """Validate and parse decimal string."""
    if not value:
        raise ValueError("Input cannot be empty")
    try:
        return Decimal(value)
    except InvalidOperation:
        raise ValueError(f"Invalid decimal format: {value}")

def validate_division_by_zero(divisor: Decimal) -> None:
    """Check division by zero."""
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

# gui.py
def on_equals_click(self):
    try:
        operand1 = validate_decimal(self.previous_value)
        operand2 = validate_decimal(self.current_value)

        if self.operator == "divide":
            validate_division_by_zero(operand2)

        result = self.calculate(operand1, operand2, self.operator)
        self.show_result(result)
    except ValueError as e:
        self.show_error(str(e))
```

**Alternatives Considered**:
- Real-time validation (on each keystroke): Rejected as too restrictive (can't type "-" before number)
- No validation: Rejected as violates constitution principle III

---

### 6. Testing Strategy

**Question**: How to test tkinter application while maintaining 80% coverage?

**Decision**: Unit test business logic, manual test GUI

**Testing Layers**:

1. **Unit Tests** (test_operations.py, test_validators.py):
   - Test each arithmetic function (add, subtract, multiply, divide)
   - Test each validation function
   - Test edge cases (division by zero, invalid input, decimals, negatives)
   - **Target**: 100% coverage of operations.py and validators.py
   - **No mocking**: Pure functions, no dependencies

2. **Manual GUI Testing** (test plan document):
   - Test each button click
   - Test keyboard input
   - Test error displays
   - Test pastel colors render correctly
   - Test window resizing
   - **Why manual**: tkinter testing requires X server / display, complex setup

**Test Execution**:
```bash
# Run unit tests (business logic)
pytest --cov=src/calculator --cov-report=term-missing

# Type checking
mypy src/calculator/

# Linting
ruff check src/calculator/

# Formatting
black --check src/calculator/
```

**Coverage Strategy**:
- operations.py: 100% (pure functions, all branches)
- validators.py: 100% (error paths, all validations)
- models.py: 90%+ (dataclasses, simple logic)
- gui.py: Excluded from coverage (manual testing)
- **Overall**: 80%+ (meets constitution requirement)

**Alternatives Considered**:
- Automated GUI testing (pytest-tkinter, etc.): Rejected as complex setup, fragile tests
- No testing: Rejected as violates constitution principle IV

---

### 7. Pastel Color Palette

**Question**: How to implement pastel colors in tkinter?

**Decision**: Use hex color codes with tkinter Button/Frame bg parameter

**Color Palette**:
```python
COLORS = {
    "pastel_pink": "#FFB6C1",        # Operations buttons (+, -, *, /)
    "pastel_mint": "#B2F5E4",        # Number buttons (0-9, .)
    "pastel_lavender": "#E6E6FA",    # Window background
    "pastel_peach": "#FFDAB9",       # Equals button (=)
    "pastel_blue": "#B0C4DE",        # Clear button (C)
    "text_dark": "#333333",          # Button text
    "text_error": "#DC143C",         # Error text (crimson)
    "display_bg": "#FFFFFF",         # Display background (white for contrast)
}
```

**Implementation**:
```python
# gui.py
btn_add = tk.Button(
    parent,
    text="+",
    bg=COLORS["pastel_pink"],
    fg=COLORS["text_dark"],
    font=("Arial", 18),
    command=lambda: self.on_operator_click("+")
)
```

**Accessibility**:
- Text contrast ratio: 4.5:1 minimum (WCAG AA standard)
- Dark text (#333) on light pastel backgrounds ensures readability

**Alternatives Considered**:
- tkinter.ttk themes: Rejected as limited color customization
- Custom theme engine: Rejected as over-engineering

---

### 8. Calculator State Management

**Question**: How to manage calculator state (current value, previous value, operator)?

**Decision**: CalculatorState dataclass in models.py

**Rationale**:
- **Type safety**: Dataclass with type hints
- **Immutability option**: Use frozen=True if needed
- **Clear state transitions**: Explicit state updates
- **Testable**: State logic separate from GUI

**State Model**:
```python
# models.py
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Literal

Operator = Literal["add", "subtract", "multiply", "divide"]

@dataclass
class CalculatorState:
    current_value: str = "0"
    previous_value: str = ""
    operator: Optional[Operator] = None
    should_reset_display: bool = False
    error: Optional[str] = None

    def reset(self) -> None:
        """Reset calculator to initial state."""
        self.current_value = "0"
        self.previous_value = ""
        self.operator = None
        self.should_reset_display = False
        self.error = None
```

**State Transitions**:
```
Initial: current_value="0", previous_value="", operator=None
User enters "5": current_value="5"
User clicks "+": previous_value="5", operator="add", should_reset_display=True
User enters "3": current_value="3" (display reset)
User clicks "=": Calculate, show result in current_value, clear operator
```

**Alternatives Considered**:
- Class attributes on GUI: Rejected as mixes state and presentation
- Dictionary: Rejected as no type safety

---

## Technology Stack Summary

| Component | Technology | Rationale |
|-----------|------------|-----------|
| GUI Framework | tkinter | Standard library, cross-platform, simple |
| Business Logic | Pure Python functions | Testable, type-safe, reusable |
| Decimal Precision | decimal.Decimal | Arbitrary precision, stdlib |
| State Management | Dataclass (CalculatorState) | Type-safe, immutable option |
| Testing | pytest, mypy, black, ruff | Constitution quality gates |
| Package Manager | uv | Fast, modern Python dependency management |
| Colors | Hex codes + bg parameter | Full customization, pastel palette |
| Error Display | Inline display + color | Non-disruptive, clear feedback |

---

## Risks and Mitigations

### Risk 1: tkinter Not Available
**Risk**: Some minimal Python installations don't include tkinter
**Mitigation**: Document requirement in README, provide installation instructions

### Risk 2: Display Overflow
**Risk**: Very long numbers overflow display widget
**Mitigation**: Limit display width, truncate with ellipsis, or use scrollable Entry

### Risk 3: Keyboard Input Conflicts
**Risk**: Keyboard shortcuts might conflict with system shortcuts
**Mitigation**: Use simple bindings (numbers, operators, Enter, Escape)

### Risk 4: Decimal Context Not Set
**Risk**: Forgetting to set decimal context could cause precision issues
**Mitigation**: Set getcontext() in main.py startup, add test to verify

---

## Next Steps (Phase 1)

1. Create data-model.md (entities: Operator, CalculatorState, Calculation)
2. Create quickstart.md (setup instructions, running app, testing)
3. Update agent context with tkinter, desktop app patterns
4. Remove contracts/api.md (not applicable for desktop app)
