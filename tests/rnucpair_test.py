import os

import unittest
from rnucpair import *

test_corpus = ""

class TestRNucPair(unittest.TestCase):
    def test_thing(self):
        self.assertEqual(rnucpair.func_try(), True)

if __name__ == '__main__':
    unittest.main()