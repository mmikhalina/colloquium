"""
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(100, 201) for i in range(0, 20)]
summ = 0
for index in range(0, 20, 2):
    summ += mass[index]
print(summ)