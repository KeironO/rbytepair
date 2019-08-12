from .rnucpair import func_try, calc_pair_stats, calc_global_vocab
from typing import Tuple

# All of my methods are belong to Rust

class NucPairEncoder:
    def __init__(self, corpus: Tuple[str]):
        self.corpus = corpus
    
    def global_vocab(self) -> dict:
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
        return calc_pair_stats(self.corpus)

