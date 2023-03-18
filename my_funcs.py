def input_int(string):
    while not (num := input(string)).isdigit():
        print("Введите натуральное число.")

    return int(num)
