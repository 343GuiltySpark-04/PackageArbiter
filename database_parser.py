from os import system

import yaml
from termcolor import cprint

"""sets the default Database Path"""

db_file_path = '/usr/local/packageArbiter/db/db.yaml'


def clear():
    system('clear')


def parser(package_name, return_bit):
    """Parses The db.yaml File"""

    key_data_name = ""
    key_data_version = 0.0
    key_data_config_dir = ""
    key_data_install = ""
    key_data_uninstall = ""
    key_data_check = ""
    key_data_bin_name = ''
    key_data_cache_name = ""

    count = 0

    path = ""
    """A switch so it doesn't use the default path for unit tests"""
    if return_bit != 10:
        path = db_file_path
    elif return_bit == 10:
        path = '../tests/test.yaml'

    stream = open(path)
    data = yaml.load(stream, Loader=yaml.FullLoader)

    count_max = len(data)

    # noinspection PyUnusedLocal
    for index in data:

        dict_count = 0

        pkg_data = data[count]

        for k, v in pkg_data.items():

            if dict_count == 0:
                key_data_name = v
            elif dict_count == 1:
                key_data_version = v
            elif dict_count == 2:
                key_data_config_dir = v
            elif dict_count == 3:
                key_data_install = v
            elif dict_count == 4:
                key_data_uninstall = v
            elif dict_count == 5:
                key_data_check = v
            elif dict_count == 6:
                key_data_bin_name = v
            elif dict_count == 7:
                key_data_cache_name = v

            dict_count += 1
        count += 1

        if count == count_max:
            break
        elif key_data_name == package_name:
            break
        else:
            continue

    stream.close()

    if return_bit == 1 or return_bit == 10:
        return key_data_name
    elif return_bit == 2:
        return key_data_version
    elif return_bit == 3:
        return key_data_config_dir
    elif return_bit == 4:
        return cprint(key_data_name, 'yellow'), cprint(key_data_version, 'yellow'), cprint(key_data_config_dir,
                                                                                           'yellow')
    elif return_bit == 5:
        return key_data_install
    elif return_bit == 6:
        return key_data_uninstall
    elif return_bit == 7:
        return key_data_check
    elif return_bit == 8:
        return key_data_bin_name
    elif return_bit == 9:
        return key_data_cache_name
