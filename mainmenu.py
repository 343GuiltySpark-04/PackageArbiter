from os import system
from subprocess import getoutput

from termcolor import cprint

from cache_parser import parser_cache
from database_parser import parser
from package_handler import install, uninstall


def clear():
    system('clear')


def package_search():
    """Searches for a package in the db.yaml (using database_parser.py file then checks for its presence in the Cache
        Directory (using cache_parser.py)"""

    cprint("So what are we looking for?", 'cyan')

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
        cprint("Sorry Package Search Failed (Package Not Found in Database)", 'red', attrs=['underline'])
        main_menu_handler()

    cprint("Making Sure It's Present in The Cache....", 'cyan')

    if exists_in_cache == 1:
        cprint("Package Located!", 'yellow')
        main_menu_handler()
    elif exists_in_cache != 2:
        cprint("Sorry Package Search Failed (Package Not Found in Cache)", 'red', attrs=['underline'])
        main_menu_handler()


def install_menu():
    """asks what package to install the makes sure its not already installed then calls the package handler"""

    cprint("What Package Do You Want Installed?", 'cyan')

    user_input = input("#>")

    if user_input != parser(user_input, 1):
        cprint(
            "ERROR: No Such Package In The Database! (you can request a package to be made PackageArbiter compatible at https://github.com/343GuiltySpark-04/PackageArbiter/issues)",
            'red', attrs=['underline'])
    # main_menu_handler()

    which_cmd = 'which ' + parser(user_input, 8)

    if getoutput(which_cmd) == parser(user_input, 7):
        cprint("Package Already Installed Aborting!", 'yellow', attrs=['underline'])
        main_menu_handler()
    else:
        install(user_input)


def uninstall_menu():
    """asks what package to uninstall then makes sure its installed then calls the package handler"""

    cprint("What Package Do You Want Uninstalled?", 'cyan')

    user_input = input("#>")

    if user_input != parser(user_input, 1):
        cprint(
            "ERROR: No Such Package In The Database! (you can request a package to be made PackageArbiter compatible at https://github.com/343GuiltySpark-04/PackageArbiter/issues)",
            'red', attrs=['underline'])
        main_menu_handler()

    which_cmd = 'which ' + parser(user_input, 8)

    if getoutput(which_cmd) != parser(user_input, 7):
        cprint("Package Not Installed Aborting!", 'yellow', attrs=['underline'])
        main_menu_handler()
    else:
        uninstall(user_input)


def main_menu():
    """Main Menu (self explanatory)"""
    cprint("Welcome to PackageArbiter, Please Select an Operation.", 'blue')
    cprint("1) Package Search.", 'yellow')
    cprint("2) Install a Package.", 'yellow')
    cprint("3) Uninstall a Package.", 'yellow')
    cprint("0) Exit.", 'red')

    user_input = int(input("#>"))

    if user_input == 1:
        clear()
        package_search()
    elif user_input == 2:
        clear()
        install_menu()
    elif user_input == 3:
        clear()
        uninstall_menu()
    elif user_input == 0:
        clear()
        cprint("Goodbye!", 'cyan')
        exit()
    elif user_input > 1:
        main_menu_handler()


def main_menu_handler():
    """Handles Any Exceptions From incorrect characters"""

    try:
        main_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        main_menu_handler()
