from os import system

from termcolor import cprint

from database_parser import parser
from internal_test import dev_tests_menu_handler


def clear():
    system('clear')


def package_search():
    cprint("So who are we looking for?", 'cyan')

    user_input = input("#>")

    exists = parser(user_input, 1)

    if exists == user_input:
        clear()
        parser(user_input, 4)
        print("\n")
        main_menu_handler()
    elif exists != user_input:
        clear()
        cprint("Sorry Hostage Rescue Failed (Package Not Found)", 'red', attrs=['underline'])
        main_menu_handler()


def main_menu():
    cprint("Welcome to PackageArbiter, Please Select an Operation.", 'blue')
    cprint("1) Edit Configuration. (DEFUNCT!)", 'yellow')
    cprint("2) Dev Tests Menu.", 'yellow')
    cprint("3) Hostage (Package) Search.", 'yellow')
    cprint("0) Exit.", 'red')

    user_input = int(input("#>"))

    if user_input == 1:
        clear()
        cprint("I SAID DEFUNCT YOU IDIOT!", 'red', attrs=['underline'])
    elif user_input == 2:
        clear()
        dev_tests_menu_handler()
    elif user_input == 3:
        clear()
        package_search()
    elif user_input == 0:
        clear()
        cprint("Goodbye!", 'cyan')
        exit()
    elif user_input != 0 or user_input != 1 or user_input != 2:
        main_menu_handler()


def main_menu_handler():
    try:
        main_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        main_menu_handler()
