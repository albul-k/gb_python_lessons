print("""
1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
\n""")
str_list = list()
i_max = 2
i = 1
while i <= i_max:
    str_input = input(f"Введите произвольную строку {i} из {i_max}\n")
    str_list.append(str_input)
    i += 1
print(f"Введенные строки {str_list}")

num_list = list()
i_max = 3
i = 1
while i <= i_max:
    num_input = input(f"Введите число {i} из {i_max}\n")
    if not num_input.isdigit():
        print("Введено не число. Повторите ввод")
        continue
    else:
        num_list.append(num_input)
        i += 1
print(f"Введенные числа {num_list}")

print(""" 
\n2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
\n""")

while True:
    seconds_input = input("Введите время в секнудах\n")
    if seconds_input.isdecimal():
        hours = int(seconds_input) // 3600
        minutes = (int(seconds_input) % 3600) / 60
        seconds = (int(seconds_input) % 3600) % 60
        print(f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        break
    else:
        print("Введено некорректное значение. Повторите ввод")
