from .rnucpair import calc_pair_stats, calc_global_vocab, calc_num_symbols
from typing import Tuple
import random

# All of my methods are belong to Rust

class NucPairEncoder:
    def __init__(self, corpus: Tuple[str], limit: int = 1000,
                 num_symbols: int = 5000, min_frequency: int = 1):

        if len(corpus) > limit:
            corpus = random.sample(corpus, limit)

        self.corpus = corpus
        self.num_symbols = num_symbols
        self.min_frequency = min_frequency
        self.global_vocab = self._global_vocab()

    def _global_vocab(self) -> dict:
        """
        Calculate the global vocabulary for a given list of
        nucleotide sequences.
        """
        return calc_global_vocab(self.corpus)
    
    def pair_statistics(self) -> dict:
        """
        Calculate the total pair statistics for a given list of
        nucleotide sequences
        """
        return calc_pair_stats(list(self.global_vocab.keys()))

    def num_symbols(self, pair_statistics: dict == None) -> dict:
        if pair_statistics == None:
            pair_statistics = self.pair_statistics()
        return calc_num_symbols(pair_statistics, self.num_symbols, self.min_frequency)

