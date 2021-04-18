from os import system

import yaml
from termcolor import cprint

db_file_path = '/usr/local/packageArbiter/db/db.yaml'


def clear():
    system('clear')


def test_db_loading(dev_test_bit):
    """Tests To Make Sure Its Formatted Right (primitive until pyYAML adds a 3.9 compatible way to use try statements)"""
    stream = open(db_file_path)

    data = yaml.load(stream, Loader=yaml.FullLoader)

    if dev_test_bit == 1:
        return cprint(data, 'yellow')
    elif dev_test_bit == 2:
        for items in data:
            print(items)


def parser(package_name, return_bit):
    key_data_name = ""
    key_data_version = 0.0
    key_data_config_dir = ""

    count = 0

    stream = open(db_file_path)
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

            dict_count += 1
        count += 1

        if count == count_max:
            break
        elif key_data_name == package_name:
            break
        else:
            continue

    stream.close()

    if return_bit == 1:
        return key_data_name
    elif return_bit == 2:
        return key_data_version
    elif return_bit == 3:
        return key_data_config_dir
    elif return_bit == 4:
        return cprint(key_data_name, 'yellow'), cprint(key_data_version, 'yellow'), cprint(key_data_config_dir,
                                                                                           'yellow')
