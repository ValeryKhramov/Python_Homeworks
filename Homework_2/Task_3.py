"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
degree = int(input("Введите любое натурально число: "))
count = 1
while 2**count <= degree:
    print(f' 2 в степени {count} = {2**count}')
    count += 1