import re
from collections import defaultdict
from random import choices

class Eddy():

    def __init__(self):
        self.chain = defaultdict(lambda: defaultdict(lambda: 0))

    def influence(self, text):
        text = re.sub(r"[^a-zA-ZÀ-ÿ\s'-]", "", text).lower()
        words = text.split()
        for i in range(len(words)):
            self.chain[words[i - 1]][words[i]] += 1 / len(words)

    def speak(self, length):
        options = list(self.chain.keys())
        if (length == 0 or len(options) == 0):
            return "Je vous en prie."
        words = choices(options)
        for i in range(length - 1):
            options = list(self.chain[words[i]].keys())
            weights = list(self.chain[words[i]].values())
            words += choices(options, weights)
        words[0] = words[0].capitalize()
        return " ".join(words) + "."