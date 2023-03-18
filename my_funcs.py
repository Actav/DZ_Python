def input_number(string):
    flag = False
    number = None

    while not flag:
        number, flag = is_number(input(string))
        print("Введите число.")

    return number


def is_number(string):
    try:
        return float(string), True
    except ValueError:
        return None, False
