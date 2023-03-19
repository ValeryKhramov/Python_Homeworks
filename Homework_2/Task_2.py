"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
from random import randint

first_number, second_number = randint(1, 1000), randint(0, 1000)
sum_numbers = first_number + second_number
total_numbers = first_number * second_number
print(f"Сумма загаданных чисел равна = {sum_numbers}")
print(f'Произведение загаданных чисел равно = {total_numbers}')
for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == sum_numbers and i * j == total_numbers:
            first_number, second_number = i, j

print(f'Загаданные числа это {first_number} и {second_number}')




