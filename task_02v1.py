"""
2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

Примеры/Тесты:
4 4 -> 2 2
5 6 -> 2 3
"""
from math import sqrt


def input_int(string):
    while not (num := input(string)).isdigit():
        print("Введите натуральное число.")

    return int(num)


def main():
    summa = input_int('Enter sum: ')
    multiple = input_int('Enter mul: ')

    deference = summa ** 2 - 4 * multiple
    if deference >= 0:
        # sq = deference ** 0.5 / 2
        sq = sqrt(deference) / 2
        p = summa / 2

        x = summa - (p + sq)
        y = summa - (p - sq)

        print(f"Первое число {int(x)}, второе число {int(y)}")
    else:
        print("Решений нет!")


main()
