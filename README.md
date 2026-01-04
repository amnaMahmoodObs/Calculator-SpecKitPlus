# Calculator with Tkinter GUI

A simple, elegant calculator application built with Python and tkinter, featuring a modern teal color scheme and precise decimal arithmetic.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division
- **Decimal Precision**: Uses Python's `decimal.Decimal` for accurate floating-point arithmetic (0.1 + 0.2 = 0.3, not 0.30000000000000004)
- **Error Handling**:
  - Division by zero detection with clear error messages
  - Invalid input validation
  - Support for negative numbers
- **Modern Teal UI**: Beautiful gradient color scheme with light to dark teal shades and coral accent
- **Cross-Platform**: Runs on macOS, Windows, and Linux (tkinter is included with Python)

## Installation

### Prerequisites

- Python 3.11 or higher
- tkinter (usually included with Python)

### Setup

```bash
# Clone the repository
git clone https://github.com/amnaMahmoodObs/Calculator-SpecKitPlus.git
cd Calculator-Class9

# Install development dependencies (optional, for testing)
pip install pytest pytest-cov mypy black ruff

# Or if using uv:
uv sync --all-extras
```

## Usage

### Running the Calculator

```bash
# Method 1: Direct execution
python3 src/calculator/main.py

# Method 2: As a module
python3 -m src.calculator.main
```

### Using the Calculator

1. Click number buttons (0-9) to enter numbers
2. Use decimal point (.) for decimal numbers
3. Click operator buttons (+, -, ×, ÷) to select operation
4. Press = to calculate result
5. Press C to clear and start over

### Examples

- **Basic arithmetic**: `5 + 3 = 8`
- **Decimal precision**: `0.1 + 0.2 = 0.3`
- **Negative numbers**: `-5 + 3 = -2`
- **Division by zero**: `5 ÷ 0` → displays "Error: Cannot divide by zero"

## Development

### Running Tests

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test file
python3 -m pytest tests/test_operations.py -v
```

**Test Coverage**: 27 tests covering:
- Basic arithmetic operations
- Decimal precision
- Negative numbers
- Error handling
- State management
- Input validation

### Code Quality

```bash
# Type checking
mypy src/calculator/

# Linting
ruff check src/calculator/

# Formatting
black src/calculator/
```

## Project Structure

```
Calculator-Class9/
├── src/calculator/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Entry point
│   ├── gui.py            # Tkinter GUI components
│   ├── models.py         # CalculatorState and Calculation dataclasses
│   ├── operations.py     # Pure arithmetic functions
│   └── validators.py     # Input validation
├── tests/
│   ├── conftest.py       # Pytest fixtures
│   ├── test_models.py    # Model tests
│   ├── test_operations.py # Operation tests
│   └── test_validators.py # Validation tests
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## Technical Details

### Architecture

- **Business Logic Separation**: Pure functions in `operations.py` and `validators.py` are fully testable
- **State Management**: `CalculatorState` dataclass tracks current/previous values, operator, and errors
- **Type Safety**: Full type hints with mypy strict mode
- **Decimal Precision**: Uses `decimal.Decimal` with 28 significant digits

### Teal Color Palette

- **Light Teal** (#A0E7E5): Number buttons (0-9, .)
- **Medium Teal** (#56C596): Operator buttons (+, -, ×, ÷)
- **Dark Teal** (#3AA6B9): Equals button (=)
- **Coral** (#FF9B9B): Clear button (C) - distinctive accent color
- **Pale Teal** (#C4F1E8): Window background
- **Dark Text** (#1A1A1A): Button text for excellent contrast

## Challenges Solved

1. ✅ **Decimal handling**: Precise arithmetic using `decimal.Decimal`
2. ✅ **Division by zero**: Validation with clear error messages
3. ✅ **Negative numbers**: Full support for negative operands
4. ✅ **Invalid input**: Input validation with error display

## Troubleshooting

### macOS ViewBridge Warning

If you see this warning when running the calculator on macOS:

```
unable to obtain configuration from file:///Library/Preferences/com.apple.ViewBridge.plist
due to Error Domain=NSCocoaErrorDomain Code=260 "The file "com.apple.ViewBridge.plist"
couldn't be opened because there is no such file."
```

**This is harmless and can be safely ignored.** It's a macOS system warning related to GUI rendering preferences and doesn't affect the calculator's functionality. The calculator will work perfectly fine despite this message.

### Quick Start

Simply run:
```bash
python3 src/calculator/main.py
```

The calculator window will appear and work normally, regardless of the ViewBridge warning.

## Contributing

See `.specify/memory/constitution.md` for coding principles and guidelines.

## License

MIT License

## Repository

https://github.com/amnaMahmoodObs/Calculator-SpecKitPlus
