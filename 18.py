"""
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву 10. Заповнення масиву здійснити за допомогою клавіатури.
Mikhalina Myroslav 122D
"""

mass = []
for i in range(10):
    mass.append(int(input(f"Enter {i + 1} element: ")))
mult = 1
for i in mass:
    if i < 0:
        mult *= i
print(mass)
print(mult)