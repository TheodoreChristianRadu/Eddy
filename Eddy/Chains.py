from collections import defaultdict
from Random import choose

class Chain():
    
    def __init__(self, words = [], weight = 1):
        self.map = defaultdict(lambda: defaultdict(lambda: 0))
        for i in range(len(words)):
            self.map[words[i - 1]][words[i]] += 1
        self.weight = weight

    def __call__(self, word):
        options = list(self.map[word].keys())
        weights = list(self.map[word].values())
        return choose(options, weights) if sum(weights) != 0 else ""

    def __getitem__(self, word):
        weights = list(self.map[word].values())
        return self.weight * sum(weights)

class ChainGroup(list):

    def __init__(self):
        super().__init__([])

    def __call__(self, word):
        options = [chain(word) for chain in self]
        weights = [chain[word] for chain in self]
        return choose(options, weights) if sum(weights) != 0 else ""