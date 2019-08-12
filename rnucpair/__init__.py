from .rnucpair import func_try, calc_pair_stats, calc_global_vocab

# All of my methods are belong to Rust

class NucPairEncoder:
    def __init__(self, corpus):
        self.corpus = corpus
    
    def global_vocab(self) -> dict:
        return calc_global_vocab(self.corpus)
    
    def pair_statistics(self) -> dict:
        return calc_pair_stats(self.corpus)

