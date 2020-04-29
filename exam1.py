"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        res = ''
        for itm in self.data:
            res += f'{str(itm)}\n'
        return res

    def __add__(self, other):
        new_matrix = []
        for ind, itm in enumerate(self.data):
            tmp = [sum(i) for i in zip(self.data[ind], other.data[ind])]
            new_matrix.append(tmp)
        return new_matrix


def get_matrix_random_data(value_from: int, value_to: int, x_max: int, y_max: int) -> list:
    """Создание списка списков случайными значениями

    Arguments:
        value_from {int} -- [description]
        value_to {int} -- [description]
        x_max {int} -- [description]
        y_max {int} -- [description]

    Returns:
        list -- [description]
    """
    return [[randint(value_from, value_to) for x in range(x_max)] for y in range(y_max)]


if __name__ == '__main__':
    matrix_1 = Matrix([[randint(10, 20) for x in range(5)] for y in range(5)])
    print(matrix_1)
    matrix_2 = Matrix([[randint(20, 30) for x in range(5)] for y in range(5)])
    print(matrix_2)
    matrix_3 = matrix_1 + matrix_2
    print(matrix_3)
