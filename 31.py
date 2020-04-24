"""
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Mikhalina Myroslav 122D
"""
import numpy as np
mass = [np.random.randint(-20, 20) for j in range(10)]
zzz = list(filter(lambda x: x in range(-2, 10), mass))
print(mass)
print(zzz)
print(sum(zzz) / len(zzz))