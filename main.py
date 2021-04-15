from internal_test import run_all_internal_tests
from mainmenu import main_menu


def ask_if_run_tests():
    print("Run Internal Tests? \n Yes 1 \n No 0")

    user_input = int(input())

    if user_input == 1:
        run_all_internal_tests()
    elif user_input == 0:
        start_menu()
    elif user_input != 0 or user_input != 1:
        start_menu()


def start_menu():
    main_menu()


ask_if_run_tests()
