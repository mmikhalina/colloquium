"""
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Mikhalina Myroslav 122D
"""
mass = []
for i in range(5):
    mass.append(input(f"Enter {i + 1} прізвище: "))
bukva = input('Введіть букву: ')
for j in mass:
    if j.startswith(bukva):
        print(j)