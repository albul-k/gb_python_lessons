"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os
import my_module.my_func as my_func

my_list = my_func.get_randomint_list(10, 0, 10)

file_output = 'exam5_output.tmp'
if os.path.exists(file_output):
    os.remove(file_output)

try:
    with open(file_output, 'a', encoding='UTF-8') as f_out:
        for num in my_list:
            f_out.write(f'{num} ')
        print(sum(my_list))
except IOError:
    print("Произошла ошибка записи в файл")
