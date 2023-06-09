"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
arguments = [int(i) for i in input("Введите первый элемент арифметической прогрессии, ее разность и количество "
                                   "элементов через пробел: ").split()]

arithmetic_progression = [i for i in
                          range(arguments[0], arguments[0] + (arguments[2] - 1) * arguments[1] + 1, arguments[1])]
print(*arithmetic_progression, sep="\n")
