from subprocess import call

from termcolor import cprint


def run_setup_scripts():
    cprint("Creating Package Database Directory....", 'yellow')

    call("./scripts/create_database_dir.sh")

    cprint("Done!", 'yellow')

    cprint("Creating Package Cache Directory....", 'yellow')

    call("./scripts/make_cache_dir.sh")

    cprint("Done!", 'yellow')

    cprint("Creating Scripts Directory...", 'yellow')

    call("./scripts/create_scripts_dir.sh")

    cprint("Done!", 'yellow')

    cprint("Performing First Permissions Pass....", 'yellow')

    call("./scripts/set_dir_perms.sh")

    cprint("Done!", 'yellow')


run_setup_scripts()
