"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.n - кол-во элементов первого множества.
M - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from random import randint

size_one = int(input("Введите количество элементов  первого набора: "))
size_two = int(input("Введите количество элементов  второго набора: "))

first_list = [randint(0, 100) for _ in range(size_one)]
second_list = [randint(0, 100) for _ in range(size_two)]
result_list = first_list + second_list
result = list(set(result_list))
result.sort()

print(first_list)
print(second_list)
print(result)
