print("""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
""")


def division(a: float, b: float) -> float:
    """Функция делит число a на b

    Arguments:
        a {float} -- делимое
        b {float} -- делитель

    Returns:
        float -- результат деления
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


num = []
i = 1
while i < 3:
    while True:
        tmp = input(f'Введите число {i}: ')
        try:
            tmp = float(tmp)
        except ValueError:
            print('Введено некорректное значение. Повторите ввод\n')
            continue
        except TypeError:
            print('Введено некорректное значение. Повторите ввод\n')
            continue
        num.append(tmp)
        break
    i += 1

print(division(num[0], num[1]))
