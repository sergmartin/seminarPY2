"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4

out
[2, 5, 8, 10]
[20, 40]

in
5

out
[2, 2, 4, 8, 8]
[16, 16, 4]"""

import random


m = int(input("Введите количество элементов в списке: "))
n = []
proiz = []
for i in range(m):
    n.append(random.randint(1, 10))


for i in range(len(n)):
    while i < len(n)/2 and m > len(n)/2:
        m = m - 1
        a = n[i] * n[m]
        proiz.append(a)
        i += 1

    
print(f"исходный случайный список {n}")
print(f"список результат {proiz}")
