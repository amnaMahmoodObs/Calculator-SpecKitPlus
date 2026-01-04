"""Main entry point for the Pastel Calculator application."""

import tkinter as tk
from decimal import getcontext


def main() -> None:
    """Initialize and run the calculator application."""
    # Set decimal precision at app startup (28 significant digits)
    getcontext().prec = 28

    root = tk.Tk()
    from .gui import CalculatorGUI

    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
