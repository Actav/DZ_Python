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

summ = 0
half = len(tNum)//2

for digit in tNum[:half]:
    summ += int(digit)

for digit in tNum[half:]:
    summ -= int(digit)

print(f"{tNum} >>> {'yes' if not summ else 'no'}")

# ----------------------------------------------------------------------- #

while not (tNum := input("Введите номер билета: ")).isdigit():
    print("Номер не валиден.")

tNumArr = [int(i) for i in tNum]
half = len(tNumArr)//2

print(f"{tNum} >>> {'yes' if sum(tNumArr[:half]) == sum(tNumArr[half:]) else 'no'}")
