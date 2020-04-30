"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 

Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class ClothesAbs(ABC):

    @property
    @abstractmethod
    def clother_name(self) -> str:
        pass

    @property
    @abstractmethod
    def clother_type(self) -> str:
        pass

    @property
    @abstractmethod
    def clother_param(self) -> str:
        pass

    @abstractmethod
    def total_consumption(self) -> float:
        pass


class Clothes(ClothesAbs):

    def __init__(self, clother_name, clother_type, clother_param):
        self.__name = clother_name
        self.__type = clother_type
        self.__param = clother_param
        self.__consumption = 0

    @property
    def clother_name(self):
        return self.__name

    @property
    def clother_type(self):
        return self.__type

    @property
    def clother_param(self):
        return self.__param

    @property
    def clother_consumption(self):
        return self.__consumption

    @clother_consumption.setter
    def clother_consumption(self, value):
        self.__consumption = value

    def total_consumption(self) -> float:
        pass

    def __add__(self, other):
        return self.__consumption + other.__consumption


class Coat(Clothes):

    def total_consumption(self) -> float:
        self.clother_consumption = round((self.clother_param / 6.5) + 0.5)
        return self.clother_consumption


class Suit(Clothes):

    def total_consumption(self) -> float:
        self.clother_consumption = round((2 * self.clother_param) + 0.3)
        return self.clother_consumption


if __name__ == '__main__':

    my_coat = Coat(
        clother_name='Шерстяное пальто',
        clother_type='пальто',
        clother_param=48
    )
    print(f'{my_coat.clother_name} расход={my_coat.total_consumption()}')

    my_suit = Suit(
        clother_name='Костюм Тройка',
        clother_type='костюм',
        clother_param=170
    )
    print(f'{my_suit.clother_name} расход={my_suit.total_consumption()}')
    print(f'Суммарный расход={my_coat + my_suit}')
