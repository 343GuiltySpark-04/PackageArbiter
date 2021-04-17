import yaml


class Parser:
    db_file_stream = open(r'/usr/local/packageArbiter/db/db.yaml')

    db_data = yaml.load(db_file_stream, Loader=yaml.FullLoader)

    def test_data_load(self):
        return print(Parser.db_data)

    def get_package_version(self):
        name = self

        stream = Parser.db_file_stream

        data = yaml.load(stream)
