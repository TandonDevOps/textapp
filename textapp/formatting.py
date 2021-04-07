"""
This file takes care of our text formatting for the textapp package.
"""

import os
# import colorama  Do we really need this?

# light means light screen, so dark text!
LIGHT = "light"
DARK = "dark"
GREEN = "green"
RED = "red"
CYAN = "cyan"
BOLD = "bold"

TEXT_MENU_MODE = "TEXT_MENU_MODE"

DEF_SEP_LEN = 60
DEF_SEP_CHAR = '*'

color_scheme = os.getenv(TEXT_MENU_MODE, DARK)  # some default!

HAS_TERMCOLOR = True

try:
    from termcolor import colored # noqa
except ImportError:
    HAS_TERMCOLOR = False


def color_element(text):
    if color_scheme == DARK:
        return colored(text, CYAN, attrs=[BOLD])
    else:
        return colored(text, CYAN, attrs=[BOLD])


def color_text(text):
    if color_scheme == DARK:
        return colored(text, GREEN)
    else:
        return colored(text, RED)


def sep(in_menu=False, char=DEF_SEP_CHAR, length=DEF_SEP_LEN):
    if HAS_TERMCOLOR and in_menu:
        return color_text(char*length)
    return char*length


def title(text, in_menu=False, sep_char=DEF_SEP_CHAR, sep_length=DEF_SEP_LEN):
    seper = f"{sep(in_menu, char=DEF_SEP_CHAR, length=DEF_SEP_LEN)}"
    return f"\n{seper}\n{text}\n{seper}\n"


def main():
    print(title("Does this title get printed?"))


if __name__ == "__main__":
    main()
