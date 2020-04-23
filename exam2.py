"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_input = 'exam2_data.txt'
try:
    with open(file_input, 'r', encoding='UTF-8') as f_in:
        [print(f'строка №{num+1} слов: {len(line.split())}')
         for num, line in enumerate(f_in)]
except IOError:
    print("Произошла ошибка чтения файла")
