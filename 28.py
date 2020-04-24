"""
Знайти кількість парних елементів одновимірного масиву.
Mikhalina Myroslav 122D
"""
import numpy as np

mass = [np.random.randint(-20, 20) for i in range(10)]
a = filter(lambda i: i % 2 == 0, mass)
print(f"array: {mass}")
print(f"number of paired elements: {len(list(a))}")