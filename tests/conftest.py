"""Pytest configuration and fixtures for calculator tests."""

import pytest
from decimal import Decimal


@pytest.fixture
def sample_decimals():
    """Provide sample Decimal values for testing."""
    return {
        "zero": Decimal("0"),
        "one": Decimal("1"),
        "pi": Decimal("3.14159"),
        "negative": Decimal("-5"),
        "large": Decimal("1000000"),
    }
