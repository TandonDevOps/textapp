import text_menu as tm


def another_choice():
    print("You made a different choice")
    return True


MY_MENU = {
    tm.TITLE: tm.MAIN_MENU,
    tm.DEFAULT: 0,
    tm.CHOICES: {
        tm.CONTINUE: {tm.FUNC: tm.go_on, tm.TEXT: "Keep running the menu", },
        tm.EXIT: {tm.FUNC: tm.exit, tm.TEXT: "Exit", },
        "2": {tm.FUNC: another_choice, tm.TEXT: "A different choice", },
    },
}


def main():
    tm.run_menu_cont(MY_MENU)


if __name__ == "__main__":
    main()
