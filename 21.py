"""
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Mikhalina Myroslav 122D
"""

import random
mass = [random.uniform(50, 100) for j in range(10)]
a = int(input("enter: "))
mult = 1
for i in mass:
    if i < a:
        mult *= i
print(mass)
print(mult)