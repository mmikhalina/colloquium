"""
Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
Mikhalina Myroslav 122D
"""
mass = []
for i in range(1, 10):
    aaa = (9.8 * i**2) / 2
    mass.append(aaa)
for j in range(len(mass)):
    print({j + 1}, mass[j])
