'''
Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

Примеры/Тесты:
123 >>> Сумма чисел числа 123 равна 6
100 >>> Сумма чисел числа 100 равна 1
'''
inputNum = ''
while inputNum.isdigit() == False:
    inputNum = input("Введите число: ")

N = int(inputNum)
sum = 0
while N > 0:
    sum += N%10
    N = int(N/10)

print(f"{inputNum} >>> Сумма чисел числа {inputNum} равна {sum}")

