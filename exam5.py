"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

import uuid
import os
import json


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

    def __init__(self, manufacturer: str, techology: str):
        super().__init__(manufacturer, True, 'A4', 20, _techology=techology)


class Scaner(OfficeEquipment):

    def __init__(self, manufacturer: str, resolution: str):
        super().__init__(manufacturer, True, 'A4', 1, _resolution=resolution)


class Xerox(OfficeEquipment):

    def __init__(self, manufacturer: str, copy_speed: int):
        super().__init__(manufacturer, False, 'A3', 100, _copy_speed=copy_speed)


if __name__ == '__main__':
    my_printer = Printer('HP', 'laser')
    my_printer.add_item_to_warehouse('accounting', 5)

    my_scanner = Scaner('Canon', '1000dpi')
    my_scanner.add_item_to_warehouse('sales', 10)

    my_xerox = Xerox('Epson', 50)
    my_xerox.add_item_to_warehouse('administration', 3)

    file_output = 'exam5_output.json'
    if os.path.exists(file_output):
        os.remove(file_output)

    try:
        with open(file_output, 'w', encoding='UTF-8') as f_out:
            json.dump(Warehouse().get_items(), f_out)
    except IOError:
        print("Произошла ошибка ввода/вывода файла")
