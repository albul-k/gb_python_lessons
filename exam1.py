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
        return a / b
    except TypeError:
        return None
    except ZeroDivisionError:
        return None


a, b = input('Введите два числа через пробел\n').split()
print(division(int(a), int(b)))
