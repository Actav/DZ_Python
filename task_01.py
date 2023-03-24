"""
5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
Разрешается использовать только операцию умножения. Циклы использовать нельзя

Примеры/Тесты:
<function_name>(2,0) -> 1
<function_name>(2,1) -> 2
<function_name>(2,3) -> 8
<function_name>(2,4) -> 16
"""


def mult(a, b):
    return 1 if b == 0 else mult(a, b - 1) * a


print(mult(2, 0))
print(mult(2, 1))
print(mult(2, 3))
print(mult(2, 4))
