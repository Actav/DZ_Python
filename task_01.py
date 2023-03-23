"""
4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное
диагностическое сообщение

Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

Примеры/Тесты:
Input1: 2 4 6 8 10 12 10 8 6 4 2
Input2: 3 6 9 12 15 18
Output: 6 12     Обратите внимание: Без скобочек, в одну строку

Input1: 2 4 6 8 10 10 8 6 4 2
Input2: 3 9 12 15 18
Output: Повторяющихся чисел нет
"""


def unique_list(lst1, lst2):
    res = set(str(x) for x in (lst1 + lst2)[::-1] if x in lst1 and x in lst2)
    res_string = " ".join(res)

    return 'Повторяющихся чисел нет' if res_string == '' else res_string


list_one = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
list_two = [3, 6, 9, 12, 15, 18]
print(unique_list(list_one, list_two))

list_one = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
list_two = [3, 9, 12, 15, 18]
print(unique_list(list_one, list_two))
