import numpy as np

# Function to compute the Cartesian product of two sets
def cartesian_product(set1, set2):
    return np.array(np.meshgrid(set1, set2)).T.reshape(-1, 2)

# Example usage
A = {1, 2}
B = {'a', 'b'}

print("Cartesian Product of A and B:\n", cartesian_product(A, B))

# Real-world example: Meal combinations
main_dishes = {"Burger", "Pizza"}
drinks = {"Soda", "Juice"}

print("\nMeal Combinations:\n", cartesian_product(main_dishes, drinks))