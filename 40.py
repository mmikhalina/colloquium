"""
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Mikhalina Myroslav 122D
"""

summ = 0

mass = int(input("Enter number "))
if mass != 0:
    if mass % 2 == 0:
        summ += mass

print(summ)