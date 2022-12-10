"""Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
in
7

out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]

in
-1

out
Negative value of the number of numbers!
[]

in
10

out
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9]"""

l = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {l}")
new_l = []

"""for i in l:
    if i not in l:
        new_l.append(i)"""
for i in l:
    if l.count(i)==1:
        new_l.append(i)

print(f"Список из неповторяющихся элементов: {new_l}")
