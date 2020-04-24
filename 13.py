"""
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(-10, 10) for j in range(1, 16)]
print(mass)
print(min(mass))