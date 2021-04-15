import yaml


def load_database(test):
    with open(r'/home/tristan/Documents/pkgdata.yaml') as file:
        pkg_list = yaml.load(file, Loader=yaml.FullLoader)

        if test == 1:
            print(pkg_list)
