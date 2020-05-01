"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n***.
"""


class Cell:

    def __init__(self, num: int):
        self.__cell_number = num

    @property
    def cell_number(self):
        return self.__cell_number

    def make_order(self, x: int) -> str:
        """Метод для организации ячеек по рядам

        Arguments:
            x {int} -- натуральное число, количество ячеек в ряду

        Returns:
            str -- ряды ячеек
        """
        if not x > 0:
            return ''
        else:
            cell_order = ''
            for i in range(1, self.cell_number + 1):
                cell_order += '*'
                if i % x == 0:
                    cell_order += '\n'
            return cell_order

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        _t = self.cell_number - other.cell_number
        if (_t > 0):
            return _t
        else:
            print('Результат вычисления меньше нуля')
            return None

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        try:
            _t = self.cell_number / other.cell_number
            return round(_t)
        except ZeroDivisionError:
            print('Деление на ноль запрещено')
            return None


if __name__ == '__main__':
    cell_1 = Cell(10)
    cell_2 = Cell(20)
    cell_3 = Cell(30)
    cell_4 = Cell(0)
    cell_5 = Cell(9)

    assert cell_1 + cell_2 == 30, 'cell_1 + cell_2'
    assert cell_1 + cell_4 == 10, 'cell_1 + cell_4'
    assert cell_1 - cell_2 == None, 'cell_1 - cell_2'
    assert cell_3 - cell_1 == 20, 'cell_3 - cell_1'
    assert cell_2 * cell_3 == 600, 'cell_2 * cell_3'
    assert cell_3 * cell_4 == 0, 'cell_3 * cell_4'
    assert cell_1 / cell_2 == 0, 'cell_1 / cell_2'
    assert cell_3 / cell_1 == 3, 'cell_3 / cell_1'
    assert cell_3 / cell_5 == 3, 'cell_3 / cell_5'
    assert cell_1 / cell_4 == None, 'cell_1 / cell_4'

    _x = 5
    print(
        f'Количество ячеек {cell_2.cell_number}, количество ячеек в ряду {_x}')
    print(f'{cell_2.make_order(_x)}\n')

    _x = 7
    print(
        f'Количество ячеек {cell_3.cell_number}, количество ячеек в ряду {_x}')
    print(cell_3.make_order(_x))

    _x = 2
    print(
        f'Количество ячеек {cell_4.cell_number}, количество ячеек в ряду {_x}')
    print(cell_4.make_order(_x))

    _x = 0
    print(
        f'Количество ячеек {cell_5.cell_number}, количество ячеек в ряду {_x}')
    print(cell_5.make_order(_x))
