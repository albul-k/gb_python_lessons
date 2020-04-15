print("""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
\n""")

while True:
    num_input = input("Введите число\n")
    if num_input.isdecimal() and not int(num_input) == 0:
        num_max = 0
        i = 0
        while i <= (len(num_input)-1):
            num = int(num_input[i])
            if num > num_max:
                num_max = num
            i += 1
        print(f"Самая большая цифра {num_max}")
        break
    else:
        print("Введено некорректное значение. Повторите ввод")
