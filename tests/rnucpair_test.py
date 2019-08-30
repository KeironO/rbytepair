import unittest
from rnucpair import NucPairEncoder

class TestRNucPair(unittest.TestCase):

    def test_get_global_vocab_single(self):
        corpus = [
            "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
        ]

        npe = NucPairEncoder(corpus)

        exp = {
            corpus[0] : 1
        }

        self.assertEqual(exp[corpus[0]], npe.global_vocab[corpus[0]])

    def test_get_global_vocab__multi(self):
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

    def test_pair_stats_single(self):
        corpus = [
            "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
        ]

        npe = NucPairEncoder(corpus)

        exp = {
            "GA" : 2, "AT" : 6, "TT" : 7,
            "TG" : 2, "GG" : 3, "GT" : 5,
            "TC" : 6, "CA" : 7, "AA" :7,
            "AG" : 4, "GC" : 1, "TA" : 3,
            "CG" : 1, "CC" : 1, "AC" : 2,
            "CT" : 1, "TT¿" : 1

        }

        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, exp[k])

    def test_pair_stats_multi(self):
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

        for k, v in npe.pair_statistics().items():
            self.assertEqual(v, exp[k])

    def test_num_symbols(self):
        corpus = [
            "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
        ]

        npe = NucPairEncoder(corpus)

        print(npe.get_num_symbols())

if __name__ == '__main__':
    unittest.main()