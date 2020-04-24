"""
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(5, 500) for i in range(10)]
mult = 1
for j in mass:
    if j % 3 == 0 and j % 9 == 0:
        mult *= j
print(mass)
print(mult)