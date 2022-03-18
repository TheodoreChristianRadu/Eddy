from Text import split, combine
from collections import defaultdict
from random import choices

class Eddy():

    def __init__(self):
        self.chain = defaultdict(lambda: defaultdict(lambda: 0))
        self.influence("Je vous en prie")

    def influence(self, text):
        words = split(text)
        for i in range(len(words)):
            self.chain[words[i - 1]][words[i]] += 1

    def speak(self, length):
        words, word = [], "."
        while len(words) <= length or word != ".":
            options = list(self.chain[word].keys())
            weights = list(self.chain[word].values())
            word = choices(options, weights).pop()
            words.append(word)
        return combine(words)