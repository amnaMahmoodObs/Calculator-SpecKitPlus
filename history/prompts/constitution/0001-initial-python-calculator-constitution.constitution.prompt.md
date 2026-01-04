---
id: 0001
title: Initial Python Calculator Constitution
stage: constitution
date: 2026-01-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: unknown
command: /sp.constitution
labels: ["constitution", "setup", "python", "calculator", "uv", "type-hints"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

in this project we will be creating a calculator in python. my project will be setup with uv. we will use type hints.

## Response snapshot

Created Python Calculator Constitution v1.0.0 with six core principles:

1. **Type Safety**: All code must use type hints, validated with mypy
2. **Error Handling First**: Handle error cases explicitly before happy path
3. **Input Validation**: All user input validated before computation
4. **Test-Driven Development**: Tests written before implementation (80% coverage minimum)
5. **Single Responsibility Functions**: One function per operation, max 20 lines
6. **Decimal Precision Control**: Use decimal.Decimal for all numeric operations

Development Standards include:
- uv for package management
- Python 3.11+ required
- black, ruff, mypy for code quality
- Quality gates: tests, type checking, linting, formatting, coverage

File organization: src/calculator/ with operations.py, validators.py, cli.py
Testing: Unit tests, integration tests, edge case coverage (division by zero, invalid input, negative numbers, decimal precision)

Constitution aligned with existing templates (plan, spec, tasks).

## Outcome

- ✅ Impact: Constitution v1.0.0 created and ratified, establishes project governance
- 🧪 Tests: None (constitution documentation only)
- 📁 Files: 1 created (.specify/memory/constitution.md)
- 🔁 Next prompts: /sp.specify to create feature specification, or begin calculator implementation following TDD principles
- 🧠 Reflection: Constitution emphasizes type safety and error handling for calculator robustness; decimal.Decimal addresses floating-point precision issues

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A (documentation artifact)
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): Apply constitution principles to first calculator feature (basic arithmetic operations)
