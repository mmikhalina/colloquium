"""
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(50, 100) for i in range(0, 21)]
print(mass)
num = float(input("Enter: "))
summ = 0
for j in mass:
    if j > num:
        summ += j
print(summ)