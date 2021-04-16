from os import system

from termcolor import cprint

from bash_scripts import run_initial_config_creation, create_db_dir
from mainmenu import main_menu_handler


def clear():
    system('clear')


def first_run():
    cprint("PERFORMING FIRST TIME HOSTAGE TASKS....", 'cyan')

    run_initial_config_creation()

    create_db_dir()

    clear()

    start_menu()


## ask if its the first time running

def ask_if_first_run():
    print("First Run? \n 1) Yes. \n 2) No.")

    user_input = int(input())

    if user_input == 1:
        first_run()
    elif user_input == 2:
        start_menu()
    elif user_input != 1 or user_input != 2:
        ask_if_first_run()


def start_menu():
    main_menu_handler()


## a try statement so it doesn't exit if you mistype
def ask_if_first_handler():
    try:
        ask_if_first_run()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        ask_if_first_handler()


ask_if_first_handler()
