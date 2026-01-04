# Quickstart Guide: Pastel Calculator with Tkinter

**Feature**: 001-calculator-frontend
**Date**: 2026-01-04 (Revised for tkinter)

## Prerequisites

- **Python**: 3.11 or higher (with tkinter - usually included)
- **uv**: Modern Python package manager ([install guide](https://github.com/astral-sh/uv))
- **Git**: Version control

## Quick Start (3 Minutes)

### 1. Clone and Setup

```bash
# Clone repository
git clone https://github.com/amnaMahmoodObs/Calculator-SpecKitPlus.git
cd Calculator-SpecKitPlus

# Checkout feature branch
git checkout 001-calculator-frontend

# Initialize uv project
uv init

# Install dependencies (only dev tools needed)
uv sync --all-extras
```

### 2. Run Calculator

```bash
# Run calculator application
uv run python -m src.calculator.main

# Or run directly (after activating venv)
python src/calculator/main.py
```

**Expected**: Tkinter window opens with pastel-colored calculator

### 3. Test the Calculator

1. Calculator window appears with pastel buttons
2. Try: Click `5`, `+`, `3`, `=` → Display shows `8`
3. Try: `0.1`, `+`, `0.2`, `=` → Display shows `0.3` (precise!)
4. Try: `10`, `/`, `0`, `=` → Red error: "Error: Cannot divide by zero"
5. Click `C` to clear and start over

---

## Detailed Setup

### Installing tkinter

**macOS** (usually pre-installed with Python):
```bash
# If missing, install via Homebrew
brew install python-tk@3.11
```

**Ubuntu/Debian**:
```bash
sudo apt-get install python3-tk
```

**Windows**: Included with standard Python installation

**Verify tkinter**:
```bash
python3 -c "import tkinter; print('tkinter available')"
```

### Project Structure Setup

```bash
# Create project structure
mkdir -p src/calculator tests

# Create pyproject.toml
cat > pyproject.toml <<EOF
[project]
name = "calculator"
version = "0.1.0"
description = "Pastel calculator with tkinter GUI and decimal precision"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.7.0",
    "black>=23.11.0",
    "ruff>=0.1.6",
]

[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "3.11"
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src --cov-report=term-missing"
EOF

# Initialize uv
uv sync --all-extras
```

---

## Development Workflow

### Running the Application

```bash
# Method 1: Using uv
uv run python -m src.calculator.main

# Method 2: Direct execution
python src/calculator/main.py

# Method 3: After activating venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate  # Windows
python src/calculator/main.py
```

### Running Tests

```bash
# Run all tests with coverage
uv run pytest

# Run specific test file
uv run pytest tests/test_operations.py

# Run with verbose output
uv run pytest -v

# View coverage report
uv run pytest --cov-report=html
open htmlcov/index.html
```

**Expected Coverage**:
- operations.py: 100%
- validators.py: 100%
- models.py: ≥90%
- Overall: ≥80%
- gui.py: Excluded (manual testing)

### Code Quality Checks

```bash
# Type checking
uv run mypy src/calculator/

# Linting
uv run ruff check src/calculator/

# Formatting check
uv run black --check src/calculator/

# Auto-format code
uv run black src/calculator/

# Run all checks (pre-commit)
uv run mypy src/ && \
uv run ruff check src/ && \
uv run black --check src/ && \
uv run pytest
```

---

## Manual GUI Testing

### Test Checklist

- [ ] **Display**: Shows "0" on startup
- [ ] **Number entry**: Click `5`, display shows "5"
- [ ] **Decimal point**: Click `3`, `.`, `1`, `4` → display shows "3.14"
- [ ] **Addition**: `5`, `+`, `3`, `=` → displays "8"
- [ ] **Subtraction**: `10`, `-`, `4`, `=` → displays "6"
- [ ] **Multiplication**: `7`, `*`, `6`, `=` → displays "42"
- [ ] **Division**: `20`, `/`, `4`, `=` → displays "5"
- [ ] **Decimal precision**: `0.1`, `+`, `0.2`, `=` → displays "0.3" (not 0.30000000000000004)
- [ ] **Negative numbers**: `-5`, `+`, `3`, `=` → displays "-2"
- [ ] **Division by zero**: `5`, `/`, `0`, `=` → red error "Error: Cannot divide by zero"
- [ ] **Invalid input recovery**: After error, click `C`, display resets to "0" in black
- [ ] **Clear button**: Any calculation, click `C` → resets to "0"
- [ ] **Pastel colors**: Buttons show pastel colors (pink/mint/peach/blue/lavender)
- [ ] **Window resize**: Calculator layout remains usable when resized

### Keyboard Testing (if implemented)

- [ ] Number keys `0-9` work
- [ ] `.` (decimal point) works
- [ ] `+`, `-`, `*`, `/` (operators) work
- [ ] `Enter` or `=` triggers calculation
- [ ] `Escape` or `C` clears calculator

---

## Troubleshooting

### tkinter Not Found

**Problem**: `ModuleNotFoundError: No module named 'tkinter'`

**Solution**:
```bash
# macOS
brew install python-tk@3.11

# Ubuntu/Debian
sudo apt-get install python3-tk

# Windows
# Reinstall Python with "tcl/tk and IDLE" option checked
```

---

### Display Not Updating

**Problem**: Button clicks don't update display

**Solution**:
1. Check `update_display()` is called after state changes
2. Verify `self.display.delete(0, tk.END)` and `insert()` work
3. Check event bindings: `command=lambda: self.on_number_click("5")`

---

### Colors Not Showing

**Problem**: Buttons are default gray, not pastel

**Solution**:
1. Verify hex colors in COLORS dict
2. Use `tk.Button` with `bg=` parameter (not `ttk.Button` which ignores bg)
3. Example: `tk.Button(parent, text="+", bg="#FFB6C1", fg="#333")`

---

### Decimal Precision Errors

**Problem**: `0.1 + 0.2` shows `0.30000000000000004`

**Solution**:
1. Ensure `from decimal import Decimal, getcontext` in main.py
2. Set `getcontext().prec = 28` at startup
3. Use `Decimal("0.1")` not `Decimal(0.1)` (string constructor!)
4. Normalize results: `str(result.normalize())`

---

## Configuration Files

### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
*.egg-info/

# Testing
.coverage
htmlcov/
.pytest_cache/

# IDE
.vscode/
.idea/
*.swp

# macOS
.DS_Store
```

---

## Next Steps

After completing this quickstart:

1. **Review Architecture**: Read [data-model.md](./data-model.md) and [research.md](./research.md)
2. **Run `/sp.tasks`**: Generate task list for TDD implementation
3. **Implement Tests First**: Write failing tests per tasks.md
4. **Implement Features**: Make tests pass following constitution principles
5. **Quality Gates**: Ensure all checks pass (pytest, mypy, ruff, black, 80%+ coverage)

---

## Useful Commands Cheatsheet

```bash
# Setup
uv init && uv sync --all-extras

# Run calculator
uv run python -m src.calculator.main

# Testing
uv run pytest --cov=src --cov-report=term-missing

# Quality checks
uv run mypy src/ && uv run ruff check src/ && uv run black --check src/

# Formatting
uv run black src/

# Clean
rm -rf .venv __pycache__ .pytest_cache .coverage htmlcov
```

---

## Support

- **Issues**: https://github.com/amnaMahmoodObs/Calculator-SpecKitPlus/issues
- **Documentation**: See `specs/001-calculator-frontend/` directory
- **Constitution**: See `.specify/memory/constitution.md` for coding principles
