print(""" 
2. Пользователь вводит время в секундах. 
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
