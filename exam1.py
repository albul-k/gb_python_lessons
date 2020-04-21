"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

new_file = 'temp1.tmp'
if os.path.exists(new_file):
    os.remove(new_file)

file = open(new_file, 'a', encoding='UTF-8')
while True:
    temp = input(
        'Введите данные (для окончания ввода введите пустую строку)\n')
    if not temp == '':
        try:
            file.write(f'{temp}\n')
        except IOError as e:
            print(e)
            file.close()
            break
    else:
        file.close()
        break
