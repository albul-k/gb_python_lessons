"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_input = 'exam2_data.txt'
try:
    with open(file_input, 'r', encoding='UTF-8') as f:
        for num, line in enumerate(f):
            print(f'{num+1}. количество слов: {len(line.split())}')
except IOError:
    print("Произошла ошибка чтения файла")
