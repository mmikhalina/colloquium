"""
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Mikhalina Myroslav 122D
"""
import numpy as np
mass1 = [np.random.randint(-20, 20) for j in range(10)]
mass2 = []
minNum = list(mass1).index(np.min(mass1))
for i in range(len(mass1)):
    if minNum < i:
        mass2.append(mass1[i])
print(mass1)
print(mass2)
print(sum(mass2) / len(mass2))