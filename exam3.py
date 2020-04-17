print("""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
""")


def my_func(a: int, b: int, c: int) -> int:
    """Вычисление суммы двух наибольших чисел из a, b, c

    Arguments:
        a {int} -- 1-ое целое число
        b {int} -- 2-ое целое число
        c {int} -- 3-е целое число

    Returns:
        int -- сумма 2-х наибольших чисел
    """
    try:
        num_max = max(a, b, c)
        num_medium = (a + b + c) - (num_max + min(a, b, c))
        return num_max + num_medium
    except TypeError:
        return None


num_list = input('Введите три целых числа через пробел\n').split()
for i in range(0, 3):
    num_list[i] = int(num_list[i])

print(my_func(num_list[0], num_list[1], num_list[2]))
