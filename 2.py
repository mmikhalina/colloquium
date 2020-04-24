"""
Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення кореня і квадратів кожного з елементів масиву.
Mikhalina Myroslav 122D
"""

from math import sqrt

X = []
X_sqrt = [] # данні для коренів
X_double = [] # данні для квадратів
for i in range(5):
    i = int(input("Input: "))
    X.append(i)
for i in X: # проводимо мат. дії над кожним елементом
    b = sqrt(i)
    X_sqrt.append(b)
    c = i**2
    X_double.append(c)
print(f"Numbers - {X}, roots - {X_sqrt},squares - {X_double}")