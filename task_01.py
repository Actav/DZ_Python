"""
Дан список целых чисел. Требуется вычислить, сколько раз встречается
некоторое число X в этом списке.

Пользователь вводит число X с клавиатуры. Список можно считать заданным.
Если такого числа в списке нет - вывести -1.

Примеры/Тесты:
Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
Output:  2

Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
Output:  -1
"""
from random import randint

from my_funcs import input_number

number = input_number('Введите число: ')
numbers_list = [randint(-10, 10) for _ in range(10)]
count_number = numbers_list.count(number)

print(numbers_list)
print(count_number if count_number > 0 else -1)
