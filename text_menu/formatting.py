
"""
This file takes care of our text formatting for the text_menu package.
"""

import os
import colorama
from termcolor import colored

# light means light screen, so dark text!
LIGHT = "light"
DARK = "dark"
GREEN = "green"
RED = "red"

TEXT_MENU_MODE = "TEXT_MENU_MODE"

DEF_SEP_LEN = 60
DEF_SEP_CHAR = '*'

color_scheme = os.getenv(TEXT_MENU_MODE, DARK)  # some default!

def color_menu(menu):
    if color_scheme == DARK:
        return colored(menu, GREEN)
    else:
        return colored(menu, RED)

def sep(char=DEF_SEP_CHAR, length=DEF_SEP_LEN):
    return char*length


def title(text, sep_char=DEF_SEP_CHAR, sep_length=DEF_SEP_LEN):
    seper = f"{sep(char=DEF_SEP_CHAR, length=DEF_SEP_LEN)}"
    return f"\n{seper}\n{text}\n{seper}\n"


def main():
    print(title("Does this title get printed?"))


if __name__ == "__main__":
    main()
