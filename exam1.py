"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calc_salary(hours, rate, bonus):
    try:
        return (int(hours) * float(rate)) + float(bonus)
    except ValueError:
        print('Uncorrect values')
        return None


try:
    _, hours, rate, bonus = argv
    print(calc_salary(hours, rate, bonus))
except ValueError:
    print('You should enter 3 numbers: hours rate bonus')
