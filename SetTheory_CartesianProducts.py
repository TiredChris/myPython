import numpy as np

def cartesian_product(set1, set2):
    return np.array(np.meshgrid(set1, set2)).T.reshape(-1, 2)

A = {1, 2}
B = {'a', 'b'}

print("Cartesian Product of A and B:\n", cartesian_product(A, B))

main_dishes = {"Burger", "Pizza"}
drinks = {"Soda", "Juice"}

print("\nMeal Combinations:\n", cartesian_product(main_dishes, drinks))
