"""
Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
Mikhalina Myroslav 122D
"""

import random
mass = [random.randint(500, 1000) for x in range(30)]
summ = 0
for i in mass:
    if i % 5 == 0 and i % 8 == 0:
        summ += i
print(mass)
print(summ)