
from sys import argv


def calc_salary(hours, rate, bonus):
    try:
        return (int(hours) * float(rate)) + float(bonus)
    except TypeError:
        return None
    except ValueError:
        return None


try:
    _, hours, rate, bonus = argv
    print(calc_salary(hours, rate, bonus))
except ValueError:
    print('You should enter 3 numbers: hours rate bonus')
