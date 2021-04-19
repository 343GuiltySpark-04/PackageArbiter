import subprocess
import sys
import unittest

from termcolor import cprint

import cache_parser
import database_parser


class PosixCheck(unittest.TestCase):
    """Makes sure its running in a posix environment (currently none functional WIP)"""

    def make_sure_posix(self):
        self.failUnless(sys.platform.startswith("linux"),
                        cprint("ERROR: PROGRAM MUST BE INSTALLED IN A POSIX ENVIRONMENT", 'red', attrs=['underline']))


class DatabaseParserTests(unittest.TestCase):
    """Tests The Database Parser"""

    def setUp(self):
        subprocess.call('../scripts/database_parser_test_setup.sh')

    def test_database_parser(self):
        self.assertEqual(database_parser.parser("foolib", 10), "foolib",
                         cprint("Database Parser Test Complete", 'yellow', attrs=['underline']))

    def tearDown(self):
        subprocess.call('../scripts/database_parser_test_clean.sh')


class CacheParserTest(unittest.TestCase):
    """Tests The Cache Parser"""

    def setUp(self):
        subprocess.call('../scripts/cache_parser_test_setup.sh')

    def test_cache_parser(self):
        self.assertEqual(cache_parser.parser_cache("foolib", 2), 1,
                         cprint("Cache Parser Test Complete", 'yellow', attrs=['underline']))

    def tearDown(self):
        subprocess.call('../scripts/cache_parser_test_clean.sh')


if __name__ == '__main__':
    """Runs The Tests"""
    unittest.main()
