"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного
"""

from itertools import count
from time import sleep

while True:
    tmp = input('Введите начальное значение счетчика: ')
    try:
        tmp = int(tmp)
        break
    except TypeError:
        print('Введено некорректное значение. Повторите ввод')

for el in count(tmp):
    print(el)
    sleep(0.5)
