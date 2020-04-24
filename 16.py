"""
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Mikhalina Myroslav 122D
"""

import random
mass = [random.randint(10, 50) for x in range(1, 16)]
b = []
for i in mass:
    if i % 7 == 0:
        b.append(i)
mult = 1
for i in b:
    mult = i * mult
print(mass)
print(b)
print(mult)