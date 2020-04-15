print(""" 
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
\n""")

while True:
    num_input = input("Введите число\n")
    if num_input.isdecimal():
        result = int(num_input) + int(str(num_input)*2) + int(str(num_input)*3)
        print(result)
        break
    else:
        print("Введено некорректное значение. Повторите ввод")
