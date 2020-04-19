"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""

import my_module.my_func as my_func

my_list = my_func.get_randomint_list(30, 0, 100)
print(f'Исходный список:\n{my_list}')

# пропускаем первый элемент списка
new_list = [
    value for ind, value in enumerate(my_list) if (ind > 0) and (my_list[ind] > my_list[ind-1])
]

print(f'Результат:\n{new_list}')
