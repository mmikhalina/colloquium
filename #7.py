"""
Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від 20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
Mikhalina Myroslav 122D
"""
import random
A = [random.randint(-20, 10) for x in range(1, 13)]
B = []
for i in A:
    if i < 0:
        i = 0
    B.append(i)
print("array1:", A)
print("array2:", B)
