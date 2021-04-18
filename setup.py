from subprocess import call

from setuptools import setup
from termcolor import cprint

setup(
    name='PackageArbiter',
    version='0.0.2',
    packages=['database_parser'],
    url='https://github.com/343GuiltySpark-04/PackageArbiter',
    license='GPL 2',
    author='Tristan Adams',
    author_email='killerdragonxs@gmail.com',
    description='a package manager for VadamOS'
)


def run_setup_scripts():
    cprint("Creating Package Database Directory....", 'yellow')

    call("./scripts/create_database_dir.sh")

    cprint("Done!", 'yellow')

    cprint("Creating Package Cache Directory....", 'yellow')

    call("./scripts/make_cache_dir/sh")

    cprint("Done!", 'yellow')


run_setup_scripts()
