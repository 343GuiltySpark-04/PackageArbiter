from os import system, name

from termcolor import cprint

from mainmenu import main_menu_handler


def check_if_posix():
    """To prevent stupidity induced issues"""

    if name != 'posix':
        cprint("WHY THE FUCK ARE YOU RUNNING THIS ON A NON POSIX SYSTEM?", 'red', attrs=['underline', 'bold'])
        exit("UNABLE TO FREE HOSTAGES REASON: NON-POSIX SYSTEM DETECTED!")


def clear():
    """This Function is present in all modules as importing it from main everytime causes import loop errors in some"""
    system('clear')


def start_menu():
    """Light this candle"""
    clear()
    main_menu_handler()


check_if_posix()
start_menu()
