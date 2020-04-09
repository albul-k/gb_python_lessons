print("""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
\n""")

while True:
    distance_start = input("Сколько вы пробежали за первый день(км)\n")
    if distance_start.isdecimal() and not int(distance_start) == 0:
        break
    else:
        print("Введено некорректное значение. Повторите ввод")

while True:
    distance_goal = input("Сколько минимум вы хотите пробегать\n")
    if distance_goal.isdecimal():
        if int(distance_goal) <= int(distance_start):
            print(
                "Введенное значение должно быть больше расстояния, которое вы пробежали за первый день. Повторите ввод")
        else:
            break
    else:
        print("Введено некорректное значение. Повторите ввод")

day = 1
distance = float(distance_start)
while True:
    distance = distance + (distance * 0.1)
    day += 1
    if distance > float(distance_goal):
        break
print(f"День, когда вы достигнете своей цели {day}")
