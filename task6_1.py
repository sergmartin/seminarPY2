"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
in
9

out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]

in
10

out
[28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
[24, 15, 23, 25]"""

from random import *

dlinaSpis = int(input("Ведите длину списка: "))

newSpis = [i for i in sample(range(1, dlinaSpis*2), dlinaSpis)]
print(f"Случайный список:  {newSpis}")

gotovo_list = [newSpis[i]
             for i in range(1, len(newSpis)) if newSpis[i] > newSpis[i-1]]
print(f"Конечный список: {gotovo_list}")