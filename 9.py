"""
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Mikhalina Myroslav 122D
"""

import numpy as np
def a():
    a = []
    for i in range(1,14):
        i = int(input(f"Введіть температуру о {i+7} годині: "))
        a.append(i)
    return a
mass = np.array(a())
position = 0
for i in mass:
    if i > 0:
        position += 1
    elif i < 0:
        fmt = i
        break
print(f"з 8 до 12 годин: {mass}, вперше зафіксовано від'ємну температуру - {fmt}, яка була знайдена о {position+8} годині :)")