"""
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Mikhalina Myroslav 122D
"""

import numpy as np

mass = [np.random.randint(10, 100) for j in range(10)]
b = filter(lambda j: j % 5 == 0, mass)
print(mass)
print("multiplication:", np.prod(list(b)))