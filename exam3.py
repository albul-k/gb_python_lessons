"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {
        'wage': 0,
        'bonus': 0
    }

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position(name='Bill', surname='Gates', position='head',
                    income={'wage': 1000000, 'bonus': 500000})

worker_2 = Position(name='Donald', surname='Trump', position='president',
                    income={'wage': 2000000, 'bonus': 100000})

if __name__ == '__main__':
    assert worker_1.get_full_name() == 'Bill Gates', 'worker_1.get_full_name()'
    assert worker_1.get_total_income() == 1500000, 'worker_1.get_total_income()'

    assert worker_2.get_full_name() == 'Donald Trump', 'worker_2.get_full_name()'
    assert worker_2.get_total_income() == 2100000, 'worker_2.get_total_income()'

    print(f'{worker_1.get_full_name()} - {worker_1.get_total_income()}')
    print(f'{worker_2.get_full_name()} - {worker_2.get_total_income()}')
