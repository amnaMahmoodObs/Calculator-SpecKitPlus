<!--
Sync Impact Report:
Version change: [none] → 1.0.0
Modified principles: Initial creation
Added sections: All core principles, Development Standards, Testing & Quality, Governance
Removed sections: None
Templates requiring updates:
  ✅ plan-template.md - aligned with constitution principles
  ✅ spec-template.md - aligned with user scenarios approach
  ✅ tasks-template.md - aligned with test-first requirements
Follow-up TODOs: None - all placeholders filled
-->

# Python Calculator Constitution

## Core Principles

### I. Type Safety

**Rule**: All Python code MUST use type hints for function parameters and return values.

**Rationale**: Type hints improve code clarity, catch errors early during development, and enable better IDE support. For a calculator handling numeric operations, explicit type declarations prevent common mistakes with numeric types (int vs float) and help validate input/output contracts.

**Requirements**:
- Every function MUST declare parameter types and return type
- Use `Union`, `Optional`, or `|` syntax for multiple type possibilities
- Type hints MUST be validated using `mypy` or similar type checker
- No `Any` type unless absolutely necessary and justified in comments

### II. Error Handling First

**Rule**: All operations MUST handle error cases explicitly before implementing happy path logic.

**Rationale**: A calculator's primary failure modes (division by zero, invalid input, numeric overflow) are well-known and predictable. Handling errors first ensures robustness and prevents silent failures or crashes.

**Requirements**:
- Division by zero MUST be caught and handled with clear error messages
- Invalid input (non-numeric, alphabets) MUST be validated before processing
- Negative number handling MUST be explicit and tested
- Decimal precision MUST be controlled and documented
- Every function MUST document error conditions in docstring

### III. Input Validation

**Rule**: All user input MUST be validated before any computation.

**Rationale**: User input is the primary attack vector for bugs. Validating input ensures data integrity and prevents downstream errors.

**Requirements**:
- Type validation MUST happen at input boundaries
- Range validation for numeric values where applicable
- Format validation for decimal inputs
- Clear error messages for validation failures
- Input validation MUST be a separate, testable function

### IV. Test-Driven Development (TDD)

**Rule**: Tests MUST be written before implementation code.

**Rationale**: TDD ensures requirements are clear, edge cases are identified early, and implementation stays focused. For a calculator, test cases directly map to requirements (operations, edge cases, error conditions).

**Requirements**:
- Write tests first, verify they fail
- Implement code to make tests pass
- Tests MUST cover: happy path, edge cases, error conditions
- Test naming convention: `test_<operation>_<scenario>`
- Minimum 80% code coverage for calculator logic

### V. Single Responsibility Functions

**Rule**: Each function MUST perform exactly one operation or validation.

**Rationale**: Simple, focused functions are easier to test, debug, and reuse. Calculator operations naturally decompose into single-responsibility units.

**Requirements**:
- One function per arithmetic operation (add, subtract, multiply, divide)
- Separate functions for input validation, parsing, formatting
- Functions MUST be no longer than 20 lines
- Complex operations MUST be decomposed into helper functions
- Function names MUST be verbs describing the single action

### VI. Decimal Precision Control

**Rule**: All decimal operations MUST use Python's `decimal.Decimal` type for accuracy.

**Rationale**: Floating-point arithmetic introduces rounding errors that are unacceptable in a calculator. The `Decimal` type provides arbitrary precision and avoids binary floating-point issues.

**Requirements**:
- Use `decimal.Decimal` for all numeric operations
- Set explicit precision context at application start
- Document precision choices in configuration
- Never use `float` for calculations (only for display formatting if needed)
- Test decimal edge cases: 0.1 + 0.2, division remainder, rounding

## Development Standards

### Code Quality

- **Formatting**: Use `black` for code formatting (line length: 88 chars)
- **Linting**: Use `ruff` for linting with strict rules enabled
- **Type Checking**: Use `mypy` in strict mode
- **Docstrings**: All public functions MUST have Google-style docstrings
- **Comments**: Explain WHY, not WHAT; avoid obvious comments

### Project Setup

- **Package Manager**: `uv` for all dependency management
- **Python Version**: Python 3.11+ required
- **Virtual Environment**: Always use virtual environments (managed by uv)
- **Dependencies**: Keep dependencies minimal; document all additions
- **Lock File**: Commit `uv.lock` for reproducible builds

### File Organization

```
src/
├── calculator/
│   ├── __init__.py
│   ├── operations.py    # Arithmetic operations
│   ├── validators.py    # Input validation
│   └── cli.py          # Command-line interface

tests/
├── test_operations.py
├── test_validators.py
└── test_integration.py
```

## Testing & Quality

### Testing Requirements

- **Unit Tests**: Test each function in isolation
- **Integration Tests**: Test complete user workflows
- **Edge Case Coverage**:
  - Division by zero
  - Invalid input (alphabets, symbols)
  - Negative numbers in all operations
  - Decimal precision (0.1 + 0.2 = 0.3)
  - Very large numbers
  - Empty/null input

### Test Execution

- Tests MUST pass before any commit
- Run `pytest` with coverage: `pytest --cov=src --cov-report=term-missing`
- CI/CD pipeline MUST run: tests, type check, linting
- No warnings allowed in test output

### Quality Gates

All commits MUST pass:
1. All tests passing (`pytest`)
2. Type checking passing (`mypy src/`)
3. Linting passing (`ruff check src/`)
4. Formatting check passing (`black --check src/`)
5. Code coverage >= 80%

## Governance

### Amendment Process

- Constitution changes require documented justification
- Major changes (principle additions/removals) require version bump
- All constitution updates MUST update dependent templates
- Changes MUST be committed separately from feature work

### Versioning

Constitution follows semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Backward-incompatible principle changes
- **MINOR**: New principles or expanded guidance
- **PATCH**: Clarifications, typos, non-semantic fixes

### Compliance

- All code reviews MUST verify constitution compliance
- Any principle violation MUST be justified in PR description
- Use `Complexity Tracking` section in plan.md for justified violations
- Constitution supersedes conflicting guidance in other documents

### Documentation

- All principles MUST be reflected in code review checklists
- Use CLAUDE.md for runtime development guidance
- Templates (spec, plan, tasks) MUST align with constitution
- Keep constitution concise; detailed guidance goes in templates

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
