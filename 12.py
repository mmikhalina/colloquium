"""
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Mikhalina Myroslav 122D
"""

import random
mass = [random.randint(-15, 5) for x in range(1, 11)]
b = 0
for i in mass:
    b += i
average = b / 11
count = 0
for i in mass:
    if i > average:
        count += 1
print(mass)
print(average)
print(count)