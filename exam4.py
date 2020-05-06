"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    _quantity = 0

    def __init__(self):
        pass

    def add_item(self):
        Warehouse._quantity += 1

    def remove_item(self):
        Warehouse._quantity -= 1


class OfficeEquipment(Warehouse):

    def __init__(self, manufacturer: str, isColor: bool, paper_size: str, capacity: int):
        self.__manufacturer = manufacturer
        self.__isColor = isColor
        self.__paper_size = paper_size
        self.__capacity = capacity
        super().add_item()

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
    my_scanner = Scaner('Canon', '1000dpi')
    my_xerox = Xerox('Epson', 50)
