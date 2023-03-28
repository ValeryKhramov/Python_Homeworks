"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from random import randint

print("Введите следующие значение -> 1. Количество элементов списка. "
      "2.Минимальный элемент. 3. Максимальный элемент.")
arguments = [int(i) for i in input("Введите через пробел -> ").split()]
first_list = [randint(0, arguments[2] * 2) for _ in range(arguments[0])]
# Первый вариант
# result_list = []
# for i in range(len(first_list)):
#     if arguments[1] <= first_list[i] <= arguments[2]:
#         result_list.append(i)

# Второй вариант
result_list = [item for item in range(len(first_list)) if arguments[1] <= first_list[item] <= arguments[2]]
print(first_list)
print(result_list)
