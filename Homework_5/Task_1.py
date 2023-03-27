"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
arguments = [int(i) for i in input("Введите число и желаемую степень числа через пробел: ").split()]


def degree(number, power):
    if power == 1:
        return number
    return degree(number, power - 1) * number


print(degree(arguments[0], arguments[1]))
