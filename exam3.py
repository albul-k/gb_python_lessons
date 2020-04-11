print("""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
""")

while True:
    num = input('Введите номер месяца от 1 до 12\n')
    if num.isdigit() and int(num) >= 1 and int(num) <= 12:
        break
    else:
        print('Введено некорректное значение. Повторите ввод\n')


list_month = ['зима', 'весна', 'лето', 'осень']
dict_month = {
    1: list_month[0],
    2: list_month[0],
    3: list_month[1],
    4: list_month[1],
    5: list_month[1],
    6: list_month[2],
    7: list_month[2],
    8: list_month[2],
    9: list_month[3],
    10: list_month[3],
    11: list_month[3],
    12: list_month[0],
}

print(dict_month[int(num)])
