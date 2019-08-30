import unittest
from rnucpair import NucPairEncoder

class TestRNucPair(unittest.TestCase):


    def test_get_global_vocab(self):
        corpus = [
            "ACTGGGGCCAA",
            "CGCCCGAGC",
            "ACTGGGGCCAA"
        ]
        
        npe = NucPairEncoder(corpus)
        
        exp = {
            "ACTGGGGCCAA" : 2,
            "CGCCCGAGC" : 1
        }    

        for k, v in npe.global_vocab.items():
            self.assertEqual(v, exp[k])


    def test_pair_stats(self):
        corpus = [
            "ACCGGTTGATC",
            "CGCCCGAGC",
            "ACTGGGGCCAA"
        ]

        # Hand crafted expected results

        exp = {
            "AC": 2, "AA¿": 1, "AG": 1,
            "TC¿": 1, "CA": 1, "TG": 2,
            "CG": 3, "CT": 1, "GC": 2,
            "GC¿": 1, "AT": 1, "GG": 4,
            "TT": 1, "GT": 1, "GA": 2,
            "CC": 4
        }
        npe = NucPairEncoder(corpus)

        print(npe.pair_statistics())

        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, exp[k])

if __name__ == '__main__':
    unittest.main()