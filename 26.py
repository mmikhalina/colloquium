"""
Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T.
Mikhalina Myroslav 122D
"""

T = []
for i in range(1, 6):
    T.append(float(input("Enter ")))
print("min =", min(T), "max =", max(T), "average =", sum(T)/len(T))
