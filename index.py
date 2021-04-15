import yaml


def load_database():
    with open(r'/home/tristan/Documents/pkgdata.yaml') as file:
        pkg_list = yaml.load(file, Loader=yaml.FullLoader)

        print(pkg_list)
