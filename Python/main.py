#!/usr/bin/env python3

# Modules
import sys

# ////////////////////////////////////////////
# //  THIS IS A PYTHON CODE TEMPLATE MODAL  //
# ////////////////////////////////////////////

# ==============================================
# | Date: 0000-00-00                           |
# ==============================================
# | Description: Python Code Template Example. |
# |                                            |
# ==============================================
# | Created By:                                |
# ==============================================

# Clear the screen
def clear_screen():
    # On Unix systems
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

# Colors
RED = "\033[31m"        # Classic RED
GREEN = "\033[32m"      # Classic GREEN
YELLOW = "\033[33m"     # Classic YELLOW
BLUE = "\033[34m"       # Classic BLUE
PURPLE = "\033[35m"     # Classic PURPLE
BG_RED = "\033[41m"     # Background RED
BG_GREEN = "\033[42m"   # Background GREEN
BG_YELLOW = "\033[43m"  # Background YELLOW
BG_BLUE = "\033[44m"    # Background BLUE
BG_PURPLE = "\033[45m"  # Background PURPLE
NE = "\033[0m"          # No color

# Functions
def template_function():
    print(f"{GREEN}Hello World!{NE}")

# Main function
def main():
    clear_screen()
    template_function()

# Call the main function
if __name__ == "__main__":
    main()
