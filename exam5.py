"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

import uuid


class Warehouse:
    _quantity = 0
    __stock = []

    def __init__(self):
        pass

    def add_item(self, department, quantity, data):
        Warehouse._quantity += 1
        Warehouse.__stock.append(
            {'department': department, 'quantity': quantity, 'data': data})


class OfficeEquipment(Warehouse):

    def __init__(self, manufacturer: str, isColor: bool, paper_size: str, capacity: int):
        self.__id = str(uuid.uuid4())
        self.__manufacturer = manufacturer
        self.__isColor = isColor
        self.__paper_size = paper_size
        self.__capacity = capacity

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def isColor(self):
        return self.__isColor

    @property
    def paper_size(self):
        return self.__paper_size

    @property
    def capacity(self):
        return self.__capacity

    def get_item_data(self):
        return {
            'id': self.__id,
            'manufacturer': self.__manufacturer,
            'isColor': self.__isColor,
            'paper_size': self.__paper_size,
            'capacity': self.__capacity,
        }


class Printer(OfficeEquipment):

    def __init__(self, manufacturer, techology: str):
        self.__techology = techology
        super().__init__(manufacturer, isColor=True, paper_size='A4', capacity=20)


class Scaner(OfficeEquipment):

    def __init__(self, manufacturer, resolution: str):
        self.__resolution = resolution
        super().__init__(manufacturer, isColor=True, paper_size='A4', capacity=1)


class Xerox(OfficeEquipment):

    def __init__(self, manufacturer, copy_speed: int):
        self.__copy_speed = copy_speed
        super().__init__(manufacturer, isColor=False, paper_size='A3', capacity=100)


if __name__ == '__main__':
    my_printer = Printer('HP', 'laser')
    my_printer.add_item('accounting', 5, my_printer.get_item_data())

    my_scanner = Scaner('Canon', '1000dpi')
    my_scanner.add_item('sales', 10, my_scanner.get_item_data())

    my_xerox = Xerox('Epson', 50)
    my_xerox.add_item('administration', 3, my_xerox.get_item_data())
