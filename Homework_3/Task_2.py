"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
"""
from random import randint
size = int(input("Введите размер списка: "))
find_number = int(input("Введите натуральное число: "))
numbers = [randint(0, find_number) for _ in range(size)]
count = 1
flag = True
print(numbers)
while count <= find_number and flag == True:
    for i in set(numbers):
        if i == find_number - count:
            print(i)
            flag = False
    count += 1

