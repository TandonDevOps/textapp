"""
This file defines a simple text menu facility.
"""
# JSON needed for menu data:
# import json

SUCCESS = 0
FUNC = "func"
TEXT = "text"
BAD_CHOICE = -999
SEP_CHAR = "*"
SEP_LEN = 40
SEP = SEP_CHAR*SEP_LEN
TAB = "    "
TITLE = "Title"
DEFAULT = "Default"
CHOICES = "Choices"
CONTINUE = 0
EXIT = 1


def go_on():
    return True


def exit():
    return False


TEST_MENU = {
    TITLE: "Main Menu",
    DEFAULT: 0,
    CHOICES: {
        CONTINUE: {FUNC: go_on, TEXT: "Continue displaying menu", },
        EXIT: {FUNC: exit, TEXT: "Exit", },
    },
}


def read_menu_file(menu_file):
    pass


def display_menu(menu):
    print(menu[TITLE])
    print(SEP)
    for key, val in menu[CHOICES].items():
        print(f"{TAB}{key}. {val[TEXT]}")
    print(SEP)


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


def run_menu(menu_file=None, menu_data=None):
    if menu_file is None and menu_data is None:
        return None
    elif menu_data is None:
        menu_data = read_menu_file(menu_file)
    result = True
    while result:
        display_menu(menu_data)
        choice = get_choice(menu_data)
        result = exec_choice(choice, menu_data)
    return SUCCESS


def main():
    run_menu(menu_data=TEST_MENU)
    return SUCCESS


if __name__ == "__main__":
    main()
