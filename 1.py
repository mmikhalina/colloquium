"""
Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
Mikhalina Myroslav 122D
"""
import numpy as np
mass = np.zeros(5)
for i in range(5):
    mass[i] = int(input())
print(sum(mass)/5)