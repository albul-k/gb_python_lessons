"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, value: str):
        self.__date = value

    @property
    def date(self):
        return self.__date

    @classmethod
    def parse_date(cls, value: str):
        return int(value.split('-')[0]), int(value.split('-')[1]), int(value.split('-')[2])

    @staticmethod
    def is_date_valid(value: str):
        day, month, year = int(value.split(
            '-')[0]), int(value.split('-')[1]), int(value.split('-')[2])
        if (year >= 1970) and (month >= 1) and (month <= 12) and (day >= 1) and (day <= 31):
            return True
        return False


if __name__ == '__main__':
    date_1 = Date('01-01-2000')
    _t0 = date_1.date
    _t1 = date_1.parse_date(_t0)
    _t2 = date_1.is_date_valid(_t0)
    print(f'Исходная дата: {_t0}')
    print(f'Преобразованная дата: {_t1}')
    print(f'Корректность даты: {_t2}')

    date_2 = Date('01-13-2000')
    date_3 = Date('01-01-1950')

    assert date_1.parse_date(date_1.date) == (1, 1, 2000), '01-01-2000'
    assert date_1.is_date_valid(date_1.date) == True, '01-01-2000 is Valid'

    assert date_2.parse_date(date_2.date) == (1, 13, 2000), '01-13-2000'
    assert date_2.is_date_valid(date_2.date) == False, '01-13-2000 isnt Valid'

    assert date_3.parse_date(date_3.date) == (1, 1, 1950), '01-01-1950'
    assert date_3.is_date_valid(date_3.date) == False, '01-01-1950 isnt Valid'
