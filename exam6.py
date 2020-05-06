"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

import uuid
import os
import json


class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    _items = []

    def __init__(self):
        pass

    def get_items(self):
        return self._items


class OfficeEquipment(Warehouse):

    def __init__(self, manufacturer: str, isColor: bool, paper_size: str, capacity: int, **kwargs):
        self._equip_id = str(uuid.uuid4())
        self._manufacturer = manufacturer
        self._isColor = isColor
        self._paper_size = paper_size
        self._capacity = capacity

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def equip_id(self):
        return self._equip_id

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def isColor(self):
        return self._isColor

    @property
    def paper_size(self):
        return self._paper_size

    @property
    def capacity(self):
        return self._capacity

    def add_item_to_warehouse(self, department: str, quantity: int):
        super()._items.append({
            'department': department,
            'quantity': quantity,
            'data': self.__dict__
        })


class Printer(OfficeEquipment):

    def __init__(self):
        super().__init__(manufacturer='HP', isColor=True,
                         paper_size='A4', capacity=20, techology='laser')


class Scaner(OfficeEquipment):

    def __init__(self):
        super().__init__(manufacturer='Canon', isColor=True,
                         paper_size='A4', capacity=1, resolution='1000dpi')


class Xerox(OfficeEquipment):

    def __init__(self):
        super().__init__(manufacturer='Epson', isColor=False,
                         paper_size='A3', capacity=100, copy_speed=3)


if __name__ == '__main__':

    while True:
        _t = input('Введите через пробел вид оргтехники 0/1/2 (printer/scaner/xerox), подразделение, количество. Для завершения программы введите q\n')
        if _t == 'q':
            break
        try:
            inp = _t.split()
            if len(inp) < 3 or not inp[0].isdigit() or inp[1] == '' or not inp[2].isdigit():
                raise MyError('Введено некорректное значение. Повторите ввод')
            elif inp[0] == '0':
                # new_printer = Printer()
                Printer().add_item_to_warehouse(inp[1], int(inp[2]))
            elif inp[0] == '1':
                # new_scanner = Scaner()
                Scaner().add_item_to_warehouse(inp[1], int(inp[2]))
            elif inp[0] == '2':
                # new_xerox = Xerox()
                Xerox().add_item_to_warehouse(inp[1], int(inp[2]))
            else:
                raise MyError(
                    'Введен некорретный вид оргтехники. Повторите ввод')
        except MyError as err:
            print(err)

    file_output = 'exam6_output.tmp'
    if os.path.exists(file_output):
        os.remove(file_output)

    try:
        with open(file_output, 'w', encoding='UTF-8') as f_out:
            json.dump(Warehouse().get_items(), f_out)
    except IOError:
        print("Произошла ошибка ввода/вывода файла")
