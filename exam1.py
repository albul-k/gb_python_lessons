"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_output = 'exam1_output.tmp'
if os.path.exists(file_output):
    os.remove(file_output)

try:
    with open(file_output, 'a', encoding='UTF-8') as f_in:
        while True:
            temp = input(
                'Введите данные (для окончания ввода введите пустую строку)\n')
            if not temp == '':
                f_in.write(f'{temp}\n')
            else:
                break
except IOError:
    print("Произошла ошибка записи в файл")
