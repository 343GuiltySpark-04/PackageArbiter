from os import system

from termcolor import cprint

from config_loader import LoadConfig


def clear():
    system('clear')


def config_editor_menu():
    cprint("Please Select An Option.", 'blue')
    cprint("1) Display Current Configuration Settings. \n 2) Edit Paths", 'yellow')

    user_input = int(input("#> "))

    if user_input == 1:
        clear()
        show_current_config()
    elif user_input == 2:
        print("placeholder")
    elif user_input != 1 or user_input != 2:
        clear()
        config_editor_menu_handler()


def show_current_config():
    text = LoadConfig.config['paths'].get()

    print(text)


def config_editor_menu_handler():
    try:
        config_editor_menu()
    except ValueError:
        cprint("YOU HAVE TO ENTER A NUMBER YOU DOLT!", 'red', attrs=['underline'])
        config_editor_menu_handler()
