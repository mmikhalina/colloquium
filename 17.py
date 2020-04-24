"""
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
Mikhalina Myroslav 122D
"""

import random
mass = [random.uniform(100, 200) for x in range(1, 21)]
summ = 0
for i in range(len(mass)):
    if i % 2 == 0:
        summ += mass[i]
print(mass)
print(summ)