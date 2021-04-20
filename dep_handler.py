from termcolor import cprint

from database_parser import parser


def call_main_menu():
    from mainmenu import main_menu_handler

    main_menu_handler()


def opt_dep_lister(package_name):
    opt_dep_list = parser(package_name, 11)

    index = 0

    for _ in opt_dep_list:
        cprint(opt_dep_list[index], 'yellow')

        index += 1


def dep_lister(package_name):
    dep_list = parser(package_name, 10)

    index = 0

    for _ in dep_list:
        cprint(dep_list[index], 'yellow', attrs=['underline'])

        index += 1


def dep_list_menu():
    from mainmenu import dep_lister_menu_handler

    cprint("Search dependency's for what package?", 'cyan')

    user_input_1 = input("#>")

    cprint("What kind of dependacny are you looking for?", 'cyan')
    cprint("NOTE: \"none\" indicates no dependency's were found.", 'cyan', attrs=['underline'])
    cprint("1) Required.", 'yellow')
    cprint("2) Optional.", 'yellow')

    user_input_2 = int(input("#>"))

    if user_input_2 == 1:
        dep_lister(user_input_1)
        call_main_menu()
    elif user_input_2 == 2:
        opt_dep_lister(user_input_1)
        call_main_menu()
    elif user_input_2 > 2 or user_input_2 < 1:
        cprint("ERROR: Invalid option you dolt!", 'red', attrs=['underline'])
        dep_lister_menu_handler()
