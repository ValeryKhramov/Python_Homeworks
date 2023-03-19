"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""
from random import randint
size = int(input("Введите размер списка: "))
count = 0
find_number = int(input("Введите число, которое необходимо найти: "))
numbers = [randint(1, find_number) for _ in range(size)]
for i in numbers:
    if find_number == i:
        count += 1

print(numbers)
if count == 0:
    print(f'Числа {find_number} в списке не обнаружено.')
else:
    print(f'Число {find_number} встречается в списке {count} раз.')
