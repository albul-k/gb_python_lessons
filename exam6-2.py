"""
6. Реализовать два небольших скрипта:
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import cycle
from time import sleep
import my_module.my_func as my_func

my_list = my_func.get_randomint_list(5, 0, 100)
print(f'Исходный список:\n{my_list}')

for itm in cycle(my_list):
    print(itm)
    sleep(0.5)
