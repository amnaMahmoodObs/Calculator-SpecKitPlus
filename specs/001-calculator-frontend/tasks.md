---

description: "Task list for Pastel Calculator with Tkinter GUI"
---

# Tasks: Pastel Calculator with Tkinter GUI

**Input**: Design documents from `/specs/001-calculator-frontend/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, research.md

**Tests**: Following TDD approach per constitution - tests written FIRST before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/calculator/`, `tests/` at repository root
- Paths shown below follow plan.md structure

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directory structure per plan.md
- [ ] T002 Initialize uv project with pyproject.toml configuration
- [ ] T003 [P] Create .gitignore for Python and IDE files
- [ ] T004 [P] Create src/calculator/__init__.py (empty module file)
- [ ] T005 [P] Create tests/conftest.py with pytest fixtures

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Create src/calculator/main.py with decimal precision configuration (getcontext().prec = 28)
- [ ] T007 [P] Define Operator type alias in src/calculator/models.py
- [ ] T008 [P] Create CalculatorState dataclass in src/calculator/models.py with reset(), set_error(), clear_error(), has_error() methods
- [ ] T009 [P] Create Calculation dataclass in src/calculator/models.py with from_state() and execute() methods

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic Operations (Priority: P1) 🎯 MVP

**Goal**: Implement core calculator functionality (add, subtract, multiply, divide) with tkinter GUI

**Independent Test**: Open calculator, click buttons to perform 5+3=8, 10-4=6, 7*6=42, 20/4=5

### Tests for User Story 1 (TDD - Write FIRST) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Write test_add() in tests/test_operations.py for addition with positive numbers
- [ ] T011 [P] [US1] Write test_subtract() in tests/test_operations.py for subtraction
- [ ] T012 [P] [US1] Write test_multiply() in tests/test_operations.py for multiplication
- [ ] T013 [P] [US1] Write test_divide() in tests/test_operations.py for division (non-zero divisor)
- [ ] T014 [P] [US1] Write test_operations_with_integers() in tests/test_operations.py for integer arithmetic

### Implementation for User Story 1

- [ ] T015 [P] [US1] Implement add(a: Decimal, b: Decimal) -> Decimal in src/calculator/operations.py
- [ ] T016 [P] [US1] Implement subtract(a: Decimal, b: Decimal) -> Decimal in src/calculator/operations.py
- [ ] T017 [P] [US1] Implement multiply(a: Decimal, b: Decimal) -> Decimal in src/calculator/operations.py
- [ ] T018 [P] [US1] Implement divide(a: Decimal, b: Decimal) -> Decimal in src/calculator/operations.py
- [ ] T019 [US1] Create CalculatorGUI class in src/calculator/gui.py with __init__(root: tk.Tk) method
- [ ] T020 [US1] Implement create_display() method in src/calculator/gui.py (Entry widget with pastel background)
- [ ] T021 [US1] Implement create_number_buttons() method in src/calculator/gui.py (0-9 buttons with pastel mint color #B2F5E4)
- [ ] T022 [US1] Implement create_operator_buttons() method in src/calculator/gui.py (+, -, *, / buttons with pastel pink #FFB6C1)
- [ ] T023 [US1] Implement create_equals_button() method in src/calculator/gui.py (= button with pastel peach #FFDAB9)
- [ ] T024 [US1] Implement create_clear_button() method in src/calculator/gui.py (C button with pastel blue #B0C4DE)
- [ ] T025 [US1] Implement update_display() method in src/calculator/gui.py (sync display with state.current_value)
- [ ] T026 [US1] Implement on_number_click(digit: str) method in src/calculator/gui.py (handle number button clicks)
- [ ] T027 [US1] Implement on_operator_click(operator: Operator) method in src/calculator/gui.py (handle operator button clicks)
- [ ] T028 [US1] Implement on_equals_click() method in src/calculator/gui.py (handle equals button click, calculate result)
- [ ] T029 [US1] Implement on_clear_click() method in src/calculator/gui.py (handle clear button click)
- [ ] T030 [US1] Update main() in src/calculator/main.py to launch CalculatorGUI with tk.Tk() and mainloop()

**Checkpoint**: At this point, User Story 1 should be fully functional - calculator can perform basic arithmetic with pastel GUI

---

## Phase 4: User Story 2 - Decimal Number Support (Priority: P2)

**Goal**: Support decimal numbers with precise arithmetic (0.1 + 0.2 = 0.3, not 0.30000000000000004)

**Independent Test**: Enter 0.1, +, 0.2, =, verify display shows exactly "0.3"; enter 5.5, *, 2.2, =, verify "12.1"

### Tests for User Story 2 (TDD - Write FIRST) ⚠️

- [ ] T031 [P] [US2] Write test_decimal_addition_precision() in tests/test_operations.py (0.1 + 0.2 = 0.3)
- [ ] T032 [P] [US2] Write test_decimal_multiplication() in tests/test_operations.py (5.5 * 2.2 = 12.1)
- [ ] T033 [P] [US2] Write test_decimal_division_exact() in tests/test_operations.py (10.5 / 2.1 = 5)
- [ ] T034 [P] [US2] Write test_decimal_division_repeating() in tests/test_operations.py (10 / 3 with precision)
- [ ] T035 [P] [US2] Write test_decimal_normalization() in tests/test_operations.py (ensure trailing zeros removed)

### Implementation for User Story 2

- [ ] T036 [US2] Add decimal point button (.) to create_number_buttons() in src/calculator/gui.py
- [ ] T037 [US2] Update on_number_click() in src/calculator/gui.py to handle decimal point (prevent multiple dots)
- [ ] T038 [US2] Update on_equals_click() in src/calculator/gui.py to normalize result (str(result.normalize()))
- [ ] T039 [US2] Test decimal precision manually: 0.1 + 0.2, 5.5 * 2.2, 10 / 3

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - basic arithmetic + decimal precision

---

## Phase 5: User Story 3 - Error Handling and Edge Cases (Priority: P3)

**Goal**: Handle division by zero, invalid input, negative numbers with clear error messages

**Independent Test**: Try 5/0 (shows red error), try abc+5 (error), try -5+3 (shows -2), click C to clear error

### Tests for User Story 3 (TDD - Write FIRST) ⚠️

- [ ] T040 [P] [US3] Write test_validate_decimal_valid() in tests/test_validators.py for valid decimal strings
- [ ] T041 [P] [US3] Write test_validate_decimal_invalid() in tests/test_validators.py (raises ValueError for "abc")
- [ ] T042 [P] [US3] Write test_validate_decimal_empty() in tests/test_validators.py (raises ValueError for "")
- [ ] T043 [P] [US3] Write test_validate_division_by_zero() in tests/test_validators.py (raises ValueError for divisor=0)
- [ ] T044 [P] [US3] Write test_add_with_negatives() in tests/test_operations.py (-5 + 3 = -2)
- [ ] T045 [P] [US3] Write test_multiply_negatives() in tests/test_operations.py (-10 * -2 = 20)
- [ ] T046 [P] [US3] Write test_calculator_state_error_handling() in tests/test_models.py (set_error, clear_error, has_error)

### Implementation for User Story 3

- [ ] T047 [P] [US3] Implement validate_decimal(value: str) -> Decimal in src/calculator/validators.py
- [ ] T048 [P] [US3] Implement validate_division_by_zero(divisor: Decimal) -> None in src/calculator/validators.py
- [ ] T049 [US3] Add negative button (-) to create_number_buttons() in src/calculator/gui.py (toggle sign)
- [ ] T050 [US3] Update on_equals_click() in src/calculator/gui.py to use validate_decimal() and catch ValueError
- [ ] T051 [US3] Update on_equals_click() in src/calculator/gui.py to use validate_division_by_zero() if operator is divide
- [ ] T052 [US3] Update on_equals_click() in src/calculator/gui.py to call state.set_error() on ValueError
- [ ] T053 [US3] Update update_display() in src/calculator/gui.py to change text color to red if has_error()
- [ ] T054 [US3] Update on_clear_click() in src/calculator/gui.py to call state.clear_error()
- [ ] T055 [US3] Test error handling manually: 10/0, abc+5, -5+3, -10*-2, clear button

**Checkpoint**: All user stories should now be independently functional - full calculator with error handling

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T056 [P] Add window title "Pastel Calculator" in src/calculator/gui.py __init__
- [ ] T057 [P] Set window background to pastel lavender (#E6E6FA) in src/calculator/gui.py
- [ ] T058 [P] Configure button fonts (Arial, 18pt) in src/calculator/gui.py
- [ ] T059 [P] Configure display font (Arial, 24pt, right-aligned) in src/calculator/gui.py
- [ ] T060 [P] Add window geometry/size (e.g., 300x400) in src/calculator/gui.py
- [ ] T061 Run full test suite with coverage: pytest --cov=src --cov-report=term-missing
- [ ] T062 Run type checking: mypy src/calculator/
- [ ] T063 Run linting: ruff check src/calculator/
- [ ] T064 Run formatting check: black --check src/calculator/
- [ ] T065 Verify 80%+ code coverage (operations.py and validators.py should be 100%)
- [ ] T066 Update README.md with project description, setup instructions, and usage
- [ ] T067 Manual GUI testing per quickstart.md checklist (all 14 items)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - US1 (P1): Can start after Foundational - No dependencies on other stories
  - US2 (P2): Can start after Foundational - Builds on US1 but independently testable
  - US3 (P3): Can start after Foundational - Builds on US1/US2 but independently testable
- **Polish (Phase 6)**: Depends on desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - Core calculator, no dependencies
- **User Story 2 (P2)**: Can start after Foundational - Adds decimal support, independent
- **User Story 3 (P3)**: Can start after Foundational - Adds error handling, independent

### Within Each User Story

- **Tests MUST be written and FAIL before implementation** (TDD principle)
- Pure functions (operations, validators) before GUI integration
- GUI components can be built in parallel (marked with [P])
- GUI event handlers after components created
- Manual testing after all components integrated

### Parallel Opportunities

- **Setup tasks**: T003, T004, T005 can run in parallel
- **Foundational tasks**: T007, T008, T009 can run in parallel (different entities)
- **US1 Tests**: T010-T014 can run in parallel (different test functions)
- **US1 Operations**: T015-T018 can run in parallel (different pure functions)
- **US1 GUI Components**: T020-T024 can run in parallel (different widgets)
- **US2 Tests**: T031-T035 can run in parallel
- **US3 Tests**: T040-T046 can run in parallel
- **US3 Validators**: T047-T048 can run in parallel
- **Polish tasks**: T056-T060 can run in parallel (different cosmetic changes)
- **Once Foundational phase completes**: All user stories (US1, US2, US3) can start in parallel if team capacity allows

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (TDD - write first):
Task T010: "Write test_add() in tests/test_operations.py"
Task T011: "Write test_subtract() in tests/test_operations.py"
Task T012: "Write test_multiply() in tests/test_operations.py"
Task T013: "Write test_divide() in tests/test_operations.py"
Task T014: "Write test_operations_with_integers() in tests/test_operations.py"

# Launch all operation implementations together (after tests written):
Task T015: "Implement add() in src/calculator/operations.py"
Task T016: "Implement subtract() in src/calculator/operations.py"
Task T017: "Implement multiply() in src/calculator/operations.py"
Task T018: "Implement divide() in src/calculator/operations.py"

# Launch all GUI component creations together:
Task T020: "Implement create_display() in src/calculator/gui.py"
Task T021: "Implement create_number_buttons() in src/calculator/gui.py"
Task T022: "Implement create_operator_buttons() in src/calculator/gui.py"
Task T023: "Implement create_equals_button() in src/calculator/gui.py"
Task T024: "Implement create_clear_button() in src/calculator/gui.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Basic Arithmetic)
   - Write tests first (T010-T014)
   - Implement operations (T015-T018)
   - Build GUI (T019-T029)
   - Integrate in main (T030)
4. **STOP and VALIDATE**: Test User Story 1 independently (5+3=8, 10-4=6, 7*6=42, 20/4=5)
5. Calculator is now a working MVP!

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently (MVP!)
3. Add User Story 2 → Test decimal precision (0.1+0.2=0.3)
4. Add User Story 3 → Test error handling (5/0 shows error)
5. Add Polish → Final touches (colors, fonts, README)
6. Each increment adds value without breaking previous functionality

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Basic Arithmetic + GUI)
   - Developer B: User Story 2 (Decimal Precision)
   - Developer C: User Story 3 (Error Handling)
3. Stories complete and integrate independently
4. Final: Team does Polish together

---

## Notes

- **[P] tasks** = different files, no dependencies, can run in parallel
- **[Story] label** maps task to specific user story for traceability
- **TDD approach**: Tests written FIRST (constitution requirement), then implementation
- **Each user story** should be independently completable and testable
- **Verify tests fail** before implementing (red-green-refactor cycle)
- **Commit after each task** or logical group
- **Stop at any checkpoint** to validate story independently
- **80%+ coverage target**: operations.py and validators.py should be 100%, GUI excluded
- **Manual GUI testing**: Use quickstart.md checklist (automated tkinter testing complex)
- **Avoid**: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Count Summary

- **Total Tasks**: 67
- **Setup**: 5 tasks
- **Foundational**: 4 tasks
- **User Story 1 (P1)**: 21 tasks (5 tests + 16 implementation)
- **User Story 2 (P2)**: 9 tasks (5 tests + 4 implementation)
- **User Story 3 (P3)**: 16 tasks (7 tests + 9 implementation)
- **Polish**: 12 tasks
- **Parallel Opportunities**: 40+ tasks marked with [P]
- **Test Coverage**: 17 test tasks (TDD approach)
