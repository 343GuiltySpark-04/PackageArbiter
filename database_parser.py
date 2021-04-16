import yaml


class Parser:
    with open(r'/usr/local/packageArbiter/db/db.yaml') as db_file:
        db = yaml.load(db_file, Loader=yaml.FullLoader)
