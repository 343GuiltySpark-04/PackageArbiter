import subprocess
import unittest

from termcolor import cprint

import cache_parser
import database_parser


class DatabaseParserTests(unittest.TestCase):

    def setUp(self):
        subprocess.call('../scripts/database_parser_test_setup.sh')

    def test_database_parser(self):
        self.assertEqual(database_parser.parser("foolib", 5), "foolib",
                         cprint("Database Parser Test Complete", 'yellow', attrs=['underline']))

    def tearDown(self):
        subprocess.call('../scripts/database_parser_test_clean.sh')


class CacheParserTest(unittest.TestCase):
    def setUp(self):
        subprocess.call('../scripts/cache_parser_test_setup.sh')

    def test_cache_parser(self):
        self.assertEqual(cache_parser.parser_cache("foolib", 2), 1,
                         cprint("Cache Parser Test Complete", 'yellow', attrs=['underline']))

    def tearDown(self):
        subprocess.call('../scripts/cache_parser_test_clean.sh')


if __name__ == '__main__':
    unittest.main()
