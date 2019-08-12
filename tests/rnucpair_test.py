import unittest
from rnucpair import NucPairEncoder

class TestRNucPair(unittest.TestCase):


    def test_get_global_vocab(self):
        corpus = [
            "ACCGGTTGATC",
            "CGCCCGAGC",
            "ACTGGGGCCAA"
        ]
        
        npe = NucPairEncoder(corpus)
        
        # Hand crafted expected results
        
        exp = {'C': 11, 'A': 6, 'G': 10, 'T': 4}
        
        for k, v in npe.global_vocab().items():
            self.assertEqual(v, exp[k])


    def test_pair_stats(self):
        corpus = [
            "ACCGGTTGATC",
            "CGCCCGAGC",
            "ACTGGGGCCAA"
        ]

        # Hand crafted expected results

        exp = {
            "CC": 4, "TT": 1, "GC": 3, "CG": 3,
            "GT": 1, "AA": 1, "GA": 2, "TG": 2,
            "GG": 4, "AT": 1, "CA": 1, "TC": 1,
            "CT": 1, "AC": 2, "AG": 1
            }

        npe = NucPairEncoder(corpus)

        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, exp[k])

if __name__ == '__main__':
    unittest.main()