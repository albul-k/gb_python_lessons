from random import randint


def get_randomint_list(x_max: int, rand_from: int, rand_to: int) -> list:
    """Возвращает список случайных чисел

    Arguments:
        x_max {int} -- количество элементов списка
        rand_from {int} -- значение ОТ
        rand_to {int} -- значение ДО

    Returns:
        list -- список случайных чисел
    """
    random_list = []
    for i in range(0, x_max):
        random_list.append(randint(rand_from, rand_to))
    return random_list


def get_randomint_matrix(x_max: int, y_max: int, rand_from: int, rand_to: int) -> list:
    """Создание двухмерной матрицы со случайными числами

    Arguments:
        x_max {int} -- количество столбцов
        y_max {int} -- количество строк
        rand_from {int} -- значение ОТ
        rand_to {int} -- значение ДО

    Returns:
        list -- двухмерная матрица со случайными числами
    """
    return [[randint(rand_from, rand_to) for x in range(x_max)] for y in range(y_max)]
