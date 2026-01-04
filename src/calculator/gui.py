"""Tkinter GUI for pastel calculator."""

import tkinter as tk
from typing import Callable
from decimal import Decimal

from .models import CalculatorState, Calculation, Operator
from .validators import validate_division_by_zero


# Teal color palette
COLORS = {
    "light_teal": "#A0E7E5",  # Number buttons - light teal
    "teal": "#56C596",  # Operator buttons - medium teal
    "dark_teal": "#3AA6B9",  # Equals button - darker teal
    "coral": "#FF9B9B",  # Clear button - coral for contrast
    "pale_teal": "#C4F1E8",  # Background - very pale teal
    "display_bg": "#FFFFFF",  # Display background
    "text": "#2C3E50",  # Default text color - dark blue-gray
    "error": "#E74C3C",  # Error text color - red
}


class CalculatorGUI:
    """Tkinter GUI for calculator application."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize calculator GUI."""
        self.root = root
        self.state = CalculatorState()

        # Configure window
        self.root.title("Calculator")
        self.root.geometry("320x420")
        self.root.configure(bg=COLORS["pale_teal"])
        self.root.resizable(False, False)

        # Configure grid weights for proper spacing
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

        # Create GUI components
        self.display = self.create_display()
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_equals_button()
        self.create_clear_button()

        # Initial display update
        self.update_display()

    def create_display(self) -> tk.Entry:
        """Create display widget (Entry with pastel background)."""
        display = tk.Entry(
            self.root,
            font=("Arial", 24),
            bg=COLORS["display_bg"],
            fg=COLORS["text"],
            justify="right",
            bd=5,
            relief="ridge",
        )
        display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            ipady=15,   # increases height
            sticky="ew"
        )
        return display


    def create_number_buttons(self) -> None:
        """Create number buttons (0-9) with light teal color."""
        # Number button layout
        numbers = [
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("0", 5, 0),
            (".", 5, 1),  # Decimal point
        ]

        for num, row, col in numbers:
            btn = tk.Button(
                self.root,
                text=num,
                font=("Arial", 20, "bold"),
                bg=COLORS["light_teal"],
                fg=COLORS["text"],
                activebackground="#8DD8D6",
                width=5,
                height=2,
                command=lambda n=num: self.on_number_click(n),
            )
            btn.grid(row=row, column=col, padx=(10, 10), pady=5, sticky="nsew")

    def create_operator_buttons(self) -> None:
        """Create operator buttons (+, -, *, /) with medium teal."""
        operators: list[tuple[str, Operator, int]] = [
            ("+", "add", 2),
            ("-", "subtract", 3),
            ("×", "multiply", 4),
            ("÷", "divide", 5),
        ]

        for symbol, op, row in operators:
            btn = tk.Button(
                self.root,
                text=symbol,
                font=("Arial", 20, "bold"),
                bg=COLORS["teal"],
                fg="#1A1A1A",
                activebackground=COLORS["dark_teal"],
                width=5,
                height=2,
                command=lambda o=op: self.on_operator_click(o),
            )
            btn.grid(row=row, column=3, padx=(10, 10), pady=5, sticky="nsew")

    def create_equals_button(self) -> None:
        """Create equals button (=) with dark teal."""
        btn = tk.Button(
            self.root,
            text="=",
            font=("Arial", 20, "bold"),
            bg=COLORS["dark_teal"],
            fg="#1A1A1A",
            activebackground=COLORS["teal"],
            width=5,
            height=2,
            command=self.on_equals_click,
        )
        btn.grid(row=5, column=2, padx=(10, 10), pady=5, sticky="nsew")

    def create_clear_button(self) -> None:
        """Create clear button (C) with coral color for contrast."""
        btn = tk.Button(
            self.root,
            text="C",
            font=("Arial", 20, "bold"),
            bg=COLORS["coral"],
            fg="#1A1A1A",
            activebackground="#FF7A7A",
            width=5,
            height=2,
            command=self.on_clear_click,
        )
        btn.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

    def update_display(self) -> None:
        """Sync display with state.current_value."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.state.current_value)

        # Change text color if error
        if self.state.has_error():
            self.display.config(fg=COLORS["error"])
        else:
            self.display.config(fg=COLORS["text"])

    def on_number_click(self, digit: str) -> None:
        """Handle number button clicks."""
        # Clear error state on new input
        if self.state.has_error():
            self.state.reset()

        # Handle decimal point - prevent multiple dots
        if digit == ".":
            if "." in self.state.current_value:
                return  # Already has decimal point

        # Reset display if needed
        if self.state.should_reset_display:
            self.state.current_value = digit
            self.state.should_reset_display = False
        elif self.state.current_value == "0" and digit != ".":
            self.state.current_value = digit
        else:
            self.state.current_value += digit

        self.update_display()

    def on_operator_click(self, operator: Operator) -> None:
        """Handle operator button clicks."""
        # If there's an error, clear it first
        if self.state.has_error():
            self.state.reset()
            return

        # If an operator is already set, calculate first (chaining)
        if self.state.operator is not None and not self.state.should_reset_display:
            self.on_equals_click()

        self.state.previous_value = self.state.current_value
        self.state.operator = operator
        self.state.should_reset_display = True

    def on_equals_click(self) -> None:
        """Handle equals button click, calculate result."""
        if self.state.operator is None:
            return  # Nothing to calculate

        try:
            calculation = Calculation.from_state(self.state)

            # Validate division by zero
            if self.state.operator == "divide":
                validate_division_by_zero(calculation.operand2)

            result = calculation.execute()

            # Update state with result (avoid scientific notation)
            # Convert to string, handling scientific notation
            result_str = str(result)
            if 'E' in result_str or 'e' in result_str:
                # Use fixed-point notation for scientific notation
                result_str = format(result, 'f')

            # Remove unnecessary trailing zeros after decimal point
            if '.' in result_str:
                result_str = result_str.rstrip('0').rstrip('.')

            self.state.current_value = result_str
            self.state.previous_value = ""
            self.state.operator = None
            self.state.clear_error()

        except ValueError as e:
            self.state.set_error(str(e))

        self.update_display()

    def on_clear_click(self) -> None:
        """Handle clear button click."""
        self.state.reset()
        self.update_display()
