import subprocess

from termcolor import cprint


def run_initial_config_creation():
    cprint("CREATING INITIAL CONFIGURATION FILE....", 'red')

    subprocess.call("./create_inital_config.sh")

    cprint("Done!", 'yellow')


def create_db_dir():
    cprint("CREATING THE PACKAGE DATABASE FILE (IF NOT ALREADY PRESENT YOU'LL NEED TO ADD THE ENTRIES MANUALLY!!!)...",
           'red')

    subprocess.call("./create_database_dir.sh")

    cprint("DONE!", 'yellow')
