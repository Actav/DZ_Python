'''
1.4 Требуется определить, можно ли от шоколадки размером
n × m долек отломить k долек, если разрешается сделать
один разлом по прямой между дольками (то есть разломить
шоколадку на два прямоугольника).

Примеры/Тесты:
3 2 4 -> yes
3 2 1 -> no
'''

nInput = ''
mInput = ''
kInput = ''

while not nInput.isdigit():
    nInput = input("Введите ширину шоколадки(долек): ")
while not mInput.isdigit():
    mInput = input("Введите длинну шоколадки(долек): ")
while not kInput.isdigit():
    kInput = input("насколько частей разделить: ")

n = int(nInput)
m = int(mInput)
k = int(kInput)

print(f"{n} {m} {k} -> {'yes' if k < n * m and ((k % n == 0) or (k % m == 0)) else 'no'}")
