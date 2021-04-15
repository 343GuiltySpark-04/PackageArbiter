from index import load_database


def test_database_loading():
    load_database(1)


def run_all_internal_tests():
    test_database_loading()
