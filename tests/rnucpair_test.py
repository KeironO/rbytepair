import os

import unittest
from rnucpair import NucPairEncoder

test_corpus = ""

class TestRNucPair(unittest.TestCase):

    def test_pair_statistics(self):
        corpus = [
            "ACCGGTTGATC",
            "CGCCCGAGC",
            "ACTGGGGCCAA"
        ]
        
        # Hand crafted expected results

        expected = {
            "CC": 4,
            "TT": 1,
            "GC": 3,
            "CG": 3,
            "GT": 1,
            "AA": 1,
            "GA": 2,
            "TG": 2,
            "GG": 4,
            "AT": 1,
            "CA": 1,
            "TC": 1,
            "CT": 1,
            "AC": 2,
            "AG": 1
            }

        npe = NucPairEncoder(corpus)

        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, expected[k])

if __name__ == '__main__':
    unittest.main()