print("""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
""")


def division(a: int, b: int) -> float:
    """[summary]

    Arguments:
        a {int} -- [description]
        b {int} -- [description]

    Returns:
        float -- [description]
    """
    try:
        c = a/b
    except ZeroDivisionError:
        print('Деление на ноль запрещено')
        return None
    return c


a, b = input('Введите два числа через пробел\n').split()
print(division(int(a), int(b)))
