from os import system

from termcolor import cprint

from index import load_database


def clear():
    system('clear')


def run_database_load_test(flip_bit):
    clear()

    load_database(flip_bit)


def dev_tests_menu():
    cprint("Please Select A Test To Run.", 'blue')
    cprint("1) Configuration Editor Test. (DEFUNCT!) \n2) Database Loading Test.", 'yellow')

    user_input = int(input("#>"))

    if user_input == 1:
        clear()
        cprint("I SAID DEFUNCT YOU DOLT!", 'red', attrs=['underline'])
    elif user_input == 2:
        run_database_load_test(1)
    elif user_input != 1 or user_input != 2:
        clear()
        dev_tests_menu_handler()


def dev_tests_menu_handler():
    try:
        dev_tests_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        dev_tests_menu_handler()
