"""Main entry point for the Teal Calculator application."""

import sys
from pathlib import Path
import tkinter as tk
from decimal import getcontext

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


def main() -> None:
    """Initialize and run the calculator application."""
    # Set decimal precision at app startup (28 significant digits)
    getcontext().prec = 28

    root = tk.Tk()
    from src.calculator.gui import CalculatorGUI

    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
