"""
This file defines a simple text menu facility.
"""
import os
# JSON needed for menu data:
import json

TEST = "test"
PROD = "prod"

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
CONTINUE = "0"
EXIT = "1"
URL0 = "/games/list"
URL1 = "/games/create"
MENUS_DIR = "../menus"

TYPE = "Type"
# types of "screens":
MENU = "Menu"
FORM = "Form"
DATA = "Data"

DATA_SET = "Retrieved data"

PROMPT = "Prompt"
VALUE = "Value"
FLDS = "Fields"

TEST_FORM_TITLE = "Test form"


def my_input(prompt):
    """
    Mock input if in test!
    """
    mode = os.getenv("RUN_ENV", PROD)
    if mode == TEST:
        return EXIT
    else:
        return input(f"{prompt}: ")


TEST_FORM = {
    TITLE: TEST_FORM_TITLE,
    FLDS: {
        "grid_height": {
            VALUE: 20,
            PROMPT: "What is the grid height?",
            "atype": "INT",
            "hival": 100,
            "lowval": 2
        },
        "grid_width": {
            VALUE: 20,
            PROMPT: "What is the grid width?",
            "atype": "INT",
            "hival": 100,
            "lowval": 2
        },
    },
}


def run_form(form):
    print(f"{form[TITLE]}\n")
    print(f"{SEP}\n")
    for fld in form[FLDS]:
        field = form[FLDS][fld]
        answer = my_input(f"{field[PROMPT]} ({field[VALUE]})")
        print(answer)
    return form


TEST_DATA = {
    TYPE: DATA,
    TITLE: DATA_SET,
    DATA: {"Rec1": {"fld0": 0, "fld1": 1}, "Rec2": {"fld0": 2, "fld1": 3}},
}


def data_repr(data):
    """
    Formats a data object for display.
    """
    data_txt = f"{data[TITLE]}\n"
    data_txt += f"{SEP}\n"
    for i, key in enumerate(data[DATA]):
        data_txt += f"{i}. {key}"
        rec = data[DATA][key]
        for val in rec.values():
            data_txt += f"\t{val}"
        data_txt += "\n"
    return data_txt


MENU_FILE = f"{MENUS_DIR}/test_menu.json"


def go_on():
    return True


def exit():
    return False


TEST_MENU = {
    TYPE: MENU,
    TITLE: MAIN_MENU,
    DEFAULT: CONTINUE,
    CHOICES: {
        CONTINUE: {FUNC: go_on, TEXT: "Continue displaying menu", },
        EXIT: {FUNC: exit, TEXT: "Exit", },
    },
}


URL_MENU = {
    TYPE: MENU,
    TITLE: MAIN_MENU,
    DEFAULT: CONTINUE,
    CHOICES: {
        "0": {URL: URL0, METHOD: "get", TEXT: "This is some URL", },
        "1": {URL: URL1, METHOD: "get", TEXT: "Some other URL", },
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
        try:
            c = my_input("Please enter a choice from the menu above")
            if not c or c.isspace():
                c = menu[DEFAULT]
        except ValueError:
            print("Please enter a number.")
    return c


def get_menu_item(choice, menu):
    return menu[CHOICES][choice]


def exec_choice(choice, menu):
    return get_menu_item(choice, menu)[FUNC]()


def run_menu_once(menu):
    """
    This function runs the menu once, just returning the choice made.
    """
    print(menu_repr(menu))
    return get_choice(menu)


def get_single_opt(menu):
    """
    Gets the full dict from a menu choice
    """
    return get_menu_item(run_menu_once(menu), menu)


def menu_data_from_file(menu_file, func_map=None):
    """
    Convert a file into in-mem menu.
    We must map the functions' names to strings.
    """
    menu_data = read_menu_file(menu_file, func_map)
    for opt in menu_data:
        if FUNC in opt:
            if func_map is None:
                print("You must provide a function map with your menu.")
                return None
    return menu_data


def run_menu_cont(menu_data):
    """
    This function runs the menu in a loop.
    It will exit when `exec_choice()` returns False.
    """
    result = True
    while result:
        choice = run_menu_once(menu_data)
        result = exec_choice(choice, menu_data)
    return SUCCESS


def main():
    run_form(TEST_FORM)
    return run_menu_cont(TEST_MENU)


if __name__ == "__main__":
    main()
