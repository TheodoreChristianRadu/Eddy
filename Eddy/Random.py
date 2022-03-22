from random import random
from itertools import accumulate
from bisect import bisect

def choose(options, weights):
        n = len(options)
        sums = list(accumulate(weights))
        total = sums[-1]
        return options[bisect(sums, random() * total, 0, n - 1)]