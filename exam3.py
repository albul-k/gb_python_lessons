"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

file_input = 'exam3_data.txt'
try:
    with open(file_input, 'r', encoding='UTF-8') as f_in:
        total_salary, num = 0, 1
        for line in f_in:
            num += 1
            salary = int(line.split('\t')[1])
            total_salary += salary
            if salary < 20000:
                name = line.split('\t')[0]
                print(f"{name} {salary}")
        print(f'\nСредняя зарплата: {round(total_salary / num)}')
except IOError:
    print("Произошла ошибка чтения файла")
