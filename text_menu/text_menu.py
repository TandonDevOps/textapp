"""
This file defines a simple text menu facility.
"""
# JSON needed for menu data:
import json

SUCCESS = 0
FAILURE = 1
FUNC = "func"
URL = "url"
METHOD = "method"
TEXT = "text"
BAD_CHOICE = -999
SEP_CHAR = "*"
SEP_LEN = 40
SEP = SEP_CHAR*SEP_LEN
TAB = "    "
TITLE = "Title"
DEFAULT = "Default"
CHOICES = "Choices"
MAIN_MENU = "Main Menu"
CONTINUE = 0
EXIT = 1
MENUS_DIR = "../menus"


def go_on():
    return True


def exit():
    print("In exit")
    return False


MENU_FILE = f"{MENUS_DIR}/test_menu.json"


TEST_MENU = {
    TITLE: MAIN_MENU,
    DEFAULT: CONTINUE,
    CHOICES: {
        CONTINUE: {FUNC: go_on, TEXT: "Continue displaying menu", },
        EXIT: {FUNC: exit, TEXT: "Exit", },
    },
}


FUNC_MAP = {
    "go_on": go_on,
    "exit": exit,
}


def read_menu_file(menu_file, func_map):
    menu = None
    try:
        with open(menu_file, 'r') as f:
            menu = json.load(f)
    except FileNotFoundError:
        print("Could not open menu file:", menu_file)
    return menu


def menu_repr(menu):
    menu_txt = ""
    menu_txt += f"{menu[TITLE]}\n"
    menu_txt += f"{SEP}\n"
    for key, val in menu[CHOICES].items():
        menu_txt += f"{TAB}{key}. {val[TEXT]}\n"
    menu_txt += f"{SEP}\n"
    return menu_txt


def is_valid_choice(choice, menu):
    return choice in menu[CHOICES]


def get_choice(menu):
    c = BAD_CHOICE
    while not is_valid_choice(c, menu):
        print("Please choose a number from the menu above:")
        try:
            c = input()
            if not c or c.isspace():
                c = menu[DEFAULT]
            else:
                c = int(c)
        except ValueError:
            print("Please enter a number.")
    return c


def exec_choice(choice, menu):
    return menu[CHOICES][choice][FUNC]()


def run_menu(menu_file=None, menu_data=None, func_map=None):
    if menu_file is None and menu_data is None:
        return None
    elif menu_data is None:
        menu_data = read_menu_file(menu_file, func_map)
        for opt in menu_data:
            if FUNC in opt:
                if func_map is None:
                    print("You must provide a function map with your menu.")
                    return FAILURE
    result = True
    while result:
        print(menu_repr(menu_data))
        choice = get_choice(menu_data)
        result = exec_choice(choice, menu_data)
    return SUCCESS


def main():
    run_menu(menu_data=TEST_MENU)
    # run_menu(menu_file=MENU_FILE, func_map=FUNC_MAP)
    return SUCCESS


if __name__ == "__main__":
    main()
