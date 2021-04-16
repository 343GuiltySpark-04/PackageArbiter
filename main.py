from os import system, name

from termcolor import cprint

from bash_scripts import run_initial_config_creation, create_db_dir
from mainmenu import main_menu_handler


## Because sometimes people are fucking idiots

def check_if_posix():
    if name != 'posix':
        cprint("WHY THE FUCK ARE YOU RUNNING THIS ON A NON POSIX SYSTEM?", 'red', attrs=['underline', 'bold'])
        exit("UNABLE TO FREE HOSTAGES REASON: NON-POSIX SYSTEM DETECTED!")


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

    # user_input = int(input())

    user_input = 2

    if user_input == 1:
        first_run()
    elif user_input == 2:
        start_menu()
    elif user_input != 1 or user_input != 2:
        ask_if_first_run()


def start_menu():
    clear()
    main_menu_handler()


## a try statement so it doesn't exit if you mistype
def ask_if_first_handler():
    try:
        ask_if_first_run()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        ask_if_first_handler()


check_if_posix()
ask_if_first_handler()
