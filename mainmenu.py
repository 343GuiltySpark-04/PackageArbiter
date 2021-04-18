from os import system

from termcolor import cprint

from cache_parser import parser_cache
from database_parser import parser
from internal_test import dev_tests_menu_handler


def clear():
    system('clear')


def package_search():
    """Searches for a package in the db.yaml file then checks for its presence in the Cache
        Directory"""

    cprint("So who are we looking for?", 'cyan')

    user_input = input("#>")

    exists_in_db = parser(user_input, 1)

    exists_in_cache = parser_cache(user_input, 2)

    if exists_in_db == user_input:
        clear()
        out_name = "Name: " + parser(user_input, 1)
        out_version = "Version: " + str(parser(user_input, 2))
        out_config_dir = "Config Dir: " + parser(user_input, 3)
        cprint(out_name, 'yellow')
        cprint(out_version, 'yellow')
        cprint(out_config_dir, 'yellow')
    elif exists_in_db != user_input:
        clear()
        cprint("Sorry Hostage Rescue Failed (Package Not Found in Database)", 'red', attrs=['underline'])
        main_menu_handler()

    cprint("Making Sure It's Present in The Cache....", 'cyan')

    if exists_in_cache == 1:
        cprint("Hostage (Package) Located!", 'yellow')
        main_menu_handler()
    elif exists_in_cache != 2:
        cprint("Sorry Hostage Rescue Failed (Package Not Found in Cache)", 'red', attrs=['underline'])
        main_menu_handler()


def main_menu():
    """Main Menu"""
    cprint("Welcome to PackageArbiter, Please Select an Operation.", 'blue')
    cprint("1) Dev Tests Menu.", 'yellow')
    cprint("2) Hostage (Package) Search.", 'yellow')
    cprint("0) Exit.", 'red')

    user_input = int(input("#>"))

    if user_input == 1:
        clear()
        dev_tests_menu_handler()
    elif user_input == 2:
        clear()
        package_search()
    elif user_input == 0:
        clear()
        cprint("Goodbye!", 'cyan')
        exit()
    elif user_input > 2:
        main_menu_handler()


def main_menu_handler():
    """Handles Any Exceptions From incorrect characters"""

    try:
        main_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        main_menu_handler()
