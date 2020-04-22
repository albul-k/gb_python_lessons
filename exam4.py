"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

file_input = 'exam4_data.txt'
file_output = 'exam4_output.tmp'
if os.path.exists(file_output):
    os.remove(file_output)

try:
    f_out = open(file_output, 'w', encoding='UTF-8')
    with open(file_input, 'r', encoding='UTF-8') as f_in:
        for line in f_in:
            new_word_list = []
            for word in line.split():
                if my_dict.get(word):
                    new_word_list.append(my_dict[word])
                else:
                    new_word_list.append(word)
            f_out.write(f'{(" ").join(new_word_list)}\n')
except IOError:
    print("Произошла ошибка ввода/вывода файла")
