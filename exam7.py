"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import os
import json

file_input = 'exam7_data.txt'
file_output = 'exam7_output.tmp'
if os.path.exists(file_output):
    os.remove(file_output)

list_result = []
try:
    with open(file_input, 'r', encoding='UTF-8') as f_in:
        total = {}
        average_profit, count = 0, 1
        for line in f_in:
            # data['comp_name', 'comp_type', 'revenue', 'costs']
            data = line.split('\t')
            comp_name, revenue, costs = data[0], int(data[2]), int(data[3])
            profit = revenue-costs
            if profit > 0:
                average_profit += profit
                count += 1
            total[comp_name] = profit
        list_result.append(total)
        list_result.append({
            'average_profit': round(average_profit / count)
        })
except IOError:
    print("Произошла ошибка чтения файла")

try:
    with open(file_output, 'w', encoding='UTF-8') as f_out:
        json.dump(list_result, f_out)
except IOError:
    print("Произошла ошибка записи файла")
