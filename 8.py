"""
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від 15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Mikhalina Myroslav 122D
"""
import random
mass = [random.randint(-15, 30) for x in range(1, 16)]
print(mass)
print('highest element:', max(mass),'index of highest element:', mass.index(max(mass)))