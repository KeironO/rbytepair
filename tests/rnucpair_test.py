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
            "ACTGGGGCCAA¿" : 2,
            "CGCCCGAGC¿" : 1
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
            'GG': 4, 'CC': 4, 'CA': 1,
            'A¿': 1, 'AC': 2, 'CT': 1,
            'AT': 1, 'TG': 2, 'CG': 3,
            'GT': 1, 'C¿': 2, 'GA': 2,
            'GC': 3, 'TT': 1, 'AG': 1,
            'AA': 1, 'TC': 1
            }

        npe = NucPairEncoder(corpus)


        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, exp[k])

if __name__ == '__main__':
    unittest.main()