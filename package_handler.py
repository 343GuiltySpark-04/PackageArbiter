import subprocess
from os import system

from termcolor import cprint

from cache_parser import parser_cache
from database_parser import parser

scripts_path = "/usr/local/packageArbiter/scripts/"


def check_for_package(package_name):
    check_bit = parser_cache(package_name, 2)

    if check_bit == 1:
        return 1
    elif check_bit == 2:
        return 2


def clear():
    system('clear')


def ask_again_install(package_name, flip_bit):
    clear()

    if flip_bit == 1:
        cprint("YOU NEED TO ENTER y OR n YOU DOLT!", 'red', attrs=['underline'])

    cprint("Are You Sure You Want To Install " + package_name + "? [y/n]", 'yellow', attrs=['underline'])

    user_input = input("#>")

    if user_input == "y" or "Y":
        return 1
    elif user_input == "n" or "N":
        return 2


def ask_again_uninstall(package_name, flip_bit):
    clear()

    if flip_bit == 1:
        cprint("YOU NEED TO ENTER y OR n YOU DOLT!", 'red', attr=['underline'])

    cprint("Are You Sure You Want To Uninstall " + package_name + "? [y/n], 'yellow", attrs=['underline'])

    user_input = input("#>")

    if user_input == "y" or "Y":
        return 1
    elif user_input == "n" or "N":
        return 2


def install(package_name):
    from main import start_menu
    ask_bit = 0

    try:
        ask_bit = ask_again_install(package_name, 0)
    except ValueError:
        ask_again_install(package_name, 1)

    if ask_bit == 1:
        clear()
    elif ask_bit == 2:
        cprint("ABORTING INSTALL!", 'red', attrs=['underline'])
        start_menu()

    install_script_path = scripts_path + parser(package_name, 5)

    which_cmd = 'which ' + parser(package_name, 8)

    cprint("Installing " + package_name + " Please Standby....", 'yellow')

    if check_for_package(package_name) == 2:
        cprint("ERROR: Package Not Found In Cache Please Make Sure To Place It In The Cache Directory!", 'red',
               attrs=['underline'])
        start_menu()

    subprocess.call(install_script_path)

    if subprocess.getoutput(which_cmd) == parser(package_name, 7):
        cprint("Installation Successful!", 'cyan', attrs=['underline'])
    else:
        cprint(
            "INSTALLATION FAILED PLEASE NOTIFY THE THE DEVS BY SUBMITTING A ISSUE AT https://github.com/343GuiltySpark-04/PackageArbiter/issues",
            'red', attrs=['bold', 'underline'])

    start_menu()


def uninstall(package_name):
    from main import start_menu
    ask_bit = 0

    try:
        ask_bit = ask_again_uninstall(package_name, 0)
    except ValueError:
        ask_again_uninstall(package_name, 1)

    if ask_bit == 1:
        clear()
    elif ask_bit == 2:
        cprint("ABORTING UNINSTALL!", 'red', attr=['underline'])

    uninstall_script_path = scripts_path + parser(package_name, 6)

    which_cmd = 'which ' + parser(package_name, 8)

    cprint("Uninstalling " + package_name + " Standby...", 'yellow')

    subprocess.call(uninstall_script_path)

    if subprocess.getoutput(which_cmd) == parser(package_name, 7):
        cprint(
            "UNINSTALLATION FAILED! PLEASE NOTIFY THE DEVS BY SUBMITTING A ISSUE AT https://github.com/343GuiltySpark-04/PackageArbiter/issues AND REINSTALL THE PACKAGE TO PREVENT ERRORS!",
            'red', attrs=['bold', 'underline'])
    else:
        cprint("Uninstallation Successful!", 'cyan', attrs=['underline'])

    start_menu()
