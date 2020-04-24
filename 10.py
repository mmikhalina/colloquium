"""
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів темпер атура опускалася нижче 10 градусів.
Mikhalina Myroslav 122D
"""

import random
mass = [random.randint(-20, 20) for x in range(1, 11)]
count = 0
for i in mass:
    if i < -10:
        count += 1
print(mass)
print(count)