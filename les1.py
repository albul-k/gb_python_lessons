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
