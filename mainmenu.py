from os import system

from termcolor import cprint

from config_editor import config_editor_menu_handler
from internal_test import dev_tests_menu_handler


def clear():
    system('clear')


def main_menu():
    cprint("Welcome to PackageArbiter, Please Select an Operation.", 'blue')
    cprint("1) Edit Configuration.", 'yellow')
    cprint("2) Dev Tests Menu.", 'yellow')
    cprint("0) Exit.", 'red')

    user_input = int(input())

    if user_input == 1:
        clear()
        config_editor_menu_handler()
    elif user_input == 2:
        clear()
        dev_tests_menu_handler()
    elif user_input == 0:
        cprint("Goodbye!", 'cyan')
    elif user_input != 0 or user_input != 1 or user_input != 2:
        main_menu_handler()


def main_menu_handler():
    try:
        main_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        main_menu_handler()
