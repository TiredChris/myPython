import numpy as np
from itertools import chain, combinations

def is_subset(A, B):
    return np.isin(A, B).all()

def generate_subsets(s):
    s = list(s)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

A = np.array([1, 2])
B = np.array([1, 2, 3, 4])

print("Is \"A\" subset of B?", is_subset(A, B))

given_set = {1, 2, 3}
print("All subsets:", generate_subsets(given_set))