"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calc_salary(hours: int, rate: float, bonus: float):
    try:
        hours, rate, bonus = int(hours), float(rate), float(bonus)
    except ValueError:
        return None

    if hours < 0 or rate < 0 or bonus < 0:
        return None
    return (hours * rate) + bonus


try:
    _, hours, rate, bonus = argv
    print(f'Заработная плата составит: {calc_salary(hours, rate, bonus)}')
except ValueError:
    print('Необходимо ввести через пробел выработку в часах, ставку в час, величину премии')

if __name__ == '__main__':
    assert calc_salary(160, 25, 200) == 4200, 'calc_salary(160, 25, 200)'
    assert calc_salary(-160, 25, 200) == None, 'calc_salary(-160, 25, 200)'
    assert calc_salary(160, -25, 200) == None, 'calc_salary(160, -25, 200)'
    assert calc_salary(160, 25, -200) == None, 'calc_salary(160, 25, -200)'
