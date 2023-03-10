'''
1.3[6]. Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
'''

tNum = ''
while not tNum.isdigit():
    tNum = input("Введите номер билета: ")

sum = 0
half = len(tNum)//2

for digit in tNum[:half]:
    sum += int(digit)

for digit in tNum[half:]:
    sum -= int(digit)

print(f"{tNum} >>> {'yes' if not sum else 'no'}")
