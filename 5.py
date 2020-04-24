"""
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Mikhalina Myroslav 122D
"""
from random import randint
a = []
b = []
for i in range(7):
    i = randint(0,10)
    a.append(i)
    b.append(i*2)
print(f"number - {a}, multiply by 2 - {b}")