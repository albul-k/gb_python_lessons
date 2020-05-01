"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

from my_module import my_func


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


if __name__ == '__main__':
    matrix_1 = Matrix(my_func.get_randomint_matrix(5, 5, 10, 20))
    print(matrix_1)

    matrix_2 = Matrix(my_func.get_randomint_matrix(5, 5, 20, 30))
    print(matrix_2)

    matrix_3 = matrix_1 + matrix_2
    print(matrix_3)
