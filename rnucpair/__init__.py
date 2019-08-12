from .rnucpair import func_try, calculate_pair_statistics

class NucPairEncoder:
    def __init__(self, corpus):
        self.corpus = corpus

    def pair_statistics(self):
        return calculate_pair_statistics(self.corpus)

