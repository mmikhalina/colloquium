"""
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Mikhalina Myroslav 122D
"""

import numpy as np
mass1 = [np.random.randint(-20, 20) for j in range(10)]
a = list(filter(lambda j: j % 2 == 0, mass1))
mass2 = []

stopNum = int(input("stop number: "))

for i in range(len(a)):
    if a[i] != stopNum:
        mass2.append(a[i])
    else:
        break
print(mass1)
print(mass2)
print(len(mass2))