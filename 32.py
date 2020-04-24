"""
Змінній t привласнити значення істина, якщо в одновимірном у масиві є
хоча б одне від’ємне і парне число.
Mikhalina Myroslav 122D
"""
import numpy as np
mass = [np.random.randint(-20, 20) for j in range(10)]
t = False
for i in range(len(mass)):
    if mass[i] < 0 and mass[i] % 2 == 0:
        t = True
print(mass)
print(t)