from Text import split, combine
from Chain import Chain, ChainGroup

class Eddy():

    def __init__(self):
        self.chains = ChainGroup()

    def influence(self, text):
        words = split(text)
        self.chains.append(Chain(words))

    def speak(self, length):
        words, word = [], "."
        while len(words) <= length or word != ".":
            word = self.chain(word)
            if word == "": break
            words.append(word)
        return combine(words)