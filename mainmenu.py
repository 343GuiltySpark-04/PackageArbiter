from termcolor import cprint


def main_menu():
    cprint("Welcome to PackageArbiter, Please Select an Operation.", 'blue')
    cprint("1) Edit Configuration.", 'yellow')
    cprint("0) Exit.", 'red')

    user_input = int(input())

    if user_input == 1:
        print("placeholder")
    elif user_input == 0:
        cprint("Goodbye!", 'cyan')
    elif user_input != 0 or user_input != 1:
        main_menu()
