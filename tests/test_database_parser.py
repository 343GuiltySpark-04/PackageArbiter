import unittest

import database_parser


class DatabaseParserTest(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(database_parser.parser("foolib", 1), "foolib")


unittest.main()
