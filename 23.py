"""
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(150, 300) for i in range(0, 20)]
print(mass)
average = sum(mass) / len(mass)
summ = 0
for j in mass:
    if j < average:
        summ += j
print(summ)