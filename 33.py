"""
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Mikhalina Myroslav 122D
"""
mass = []
count = 1
for i in range(0, 20):
    tmp = int(input("Enter "))
    mass.append(tmp)

    if tmp != 0:
       count *= tmp

print(count)
