import sympy as sp
import itertools

# Function to generate power set using recursion
def power_set_recursive(s):
    if not s:
        return [[]]
    rest = power_set_recursive(s[:-1])
    return rest + [subset + [s[-1]] for subset in rest]

# Example usage
given_set = [1, 2, 3]

# Generate power set recursively
recursive_result = power_set_recursive(given_set)
print("Power set (Recursive):", recursive_result)

# Generate power set using itertools
itertools_result = list(itertools.chain.from_iterable(itertools.combinations(given_set, r) for r in range(len(given_set) + 1)))
print("Power set (itertools):", itertools_result)