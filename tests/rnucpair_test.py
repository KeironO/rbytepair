import os

import unittest
from rnucpair import NucPairEncoder

test_corpus = ""

class TestRNucPair(unittest.TestCase):

    def test_pair_statistics(self):
        corpus = [
            "ACCGGTTGATCCTGCCGGACCCGACCGCTATCGGGGTAGGGCTAAGCCATGCGAGTCGCGCGCCCGGGGG",
            "CGCCCGGGAGCGGCGCACGGCTCAGTAACACGTGCCCAACCTACCCTCGGGAGGGGGACACCCCCGGGAA",
            "ACTGGGGCCAATCCCCCATAGGGGAAGGGCGCTGGAAGGCCCCTTCCCCAAAAGGGACCGCGGCCGATCC"
        ]
        
        npe = NucPairEncoder(corpus)
        npe.pair_statistics()

if __name__ == '__main__':
    unittest.main()