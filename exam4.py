"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_pow_1(x: float, y: int) -> float:
    """Функция возведения в степень через **

    Arguments:
        x {float} -- число
        y {int} -- степень

    Returns:
        float -- результат
    """
    try:
        if x > 0 and y < 0:
            if x == 1:
                return 1
            else:
                return x ** y
        else:
            None
    except TypeError:
        return None


def my_pow_2(x: float, y: int) -> float:
    """Функция возведения в степень без **

    Arguments:
        x {float} -- число
        y {int} -- степень

    Returns:
        float -- результат
    """
    try:
        if x > 0 and y < 0:
            if x == 1:
                return 1
            else:
                for i in range(y, -1):
                    x *= x
                return 1 / x
        else:
            None
    except TypeError:
        return None


while True:
    x = input('Введите положительное число x:')
    try:
        x = int(x)
    except ValueError:
        print('Введено некорректное значение. Повторите ввод\n')
        continue
    except TypeError:
        print('Введено некорректное значение. Повторите ввод\n')
        continue
    if x <= 0:
        print('Необходимо ввеcти положительное число\n')
    else:
        break

while True:
    y = input('Введите целое отрицательное число y:')
    try:
        y = int(y)
    except ValueError:
        print('Введено некорректное значение. Повторите ввод\n')
        continue
    except TypeError:
        print('Введено некорректное значение. Повторите ввод\n')
        continue
    if y >= 0:
        print('Необходимо ввеcти отрицательное число\n')
    else:
        break

print(f'Результат вычисления через **: {my_pow_1(x, y)}')
print(f'Результат вычисления без **: {my_pow_2(x, y)}')
