"""
Дано два лінійних масиву однаково ї розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однак овим індексом.
Mikhalina Myroslav 122D
"""
import numpy as np
mass1 = [np.random.randint(-20, 20) for i in range(10)]
mass2 = [np.random.randint(-20, 20) for i in range(10)]
print(mass1)
print(mass2)
print(np.multiply(mass1, mass2))