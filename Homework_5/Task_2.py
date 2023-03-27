"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""
arguments = [int(i) for i in input("Введите числа для суммы через пробел: ").split()]


def summa(number_1, number_2):
    if number_2 == 0:
        return number_1
    return summa(number_1, number_2 - 1) + 1


print(summa(arguments[0], arguments[1]))
