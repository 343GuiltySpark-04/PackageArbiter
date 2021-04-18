import pathlib
from os import system

from database_parser import parser

cache_path = '/usr/local/packageArbiter/cache'


def clear():
    system('clear')


def parser_cache(package_name, flip_bit):
    """Parses the Cache For a package"""

    full_package_name = '**/' + parser(package_name, 1) + '.tar*'

    cross_ref_name = parser(package_name, 1)

    if cross_ref_name != package_name and flip_bit == 1:
        return "ERROR: NO SUCH HOSTAGE (PACKAGE) ON FILE!"
    elif cross_ref_name != package_name and flip_bit == 2:
        return 2

    path = pathlib.Path(cache_path)

    package_list = list(path.glob(full_package_name))

    index = 0

    return_name = ""

    index_max = len(package_list)

    for _ in package_list:

        return_name = package_list[index]

        index += 1

        if index == index_max or index > index_max:
            break
        else:
            continue
    if flip_bit == 1:
        return return_name
    elif flip_bit == 2:
        return 1