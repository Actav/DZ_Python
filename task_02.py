"""
3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент
к заданному числу X. Пользователь вводит это число с клавиатуры, список можно
считать заданным. Введенное число не обязательно содержится в списке.

Примеры/Тесты:
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
Output: 2
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
Output: 10
"""

from random import randint

from my_funcs import input_number

number = input_number('Введите число: ')
numbers_list = [randint(-10, 10) for _ in range(10)]

print(numbers_list)
print(min(numbers_list, key=lambda x: abs(x - number)))
