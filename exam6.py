"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

import re

file_input = 'exam6_data.txt'

try:
    with open(file_input, 'r', encoding='UTF-8') as f_in:
        dict_subjects = {}
        for line in f_in:
            subject = line.split(':')[0]
            hours = [int(itm)
                     for itm in re.findall('\d+', line.split(':')[1])]
            dict_subjects[subject] = sum(hours)
        print(dict_subjects)
except IOError:
    print("Произошла ошибка чтения файла")
