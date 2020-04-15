print("""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
\n""")

while True:
    revenue_input = input("Введите значение выручки\n")
    if revenue_input.isdecimal():
        break
    else:
        print("Введено некорректное значение. Повторите ввод")

while True:
    costs_input = input("Введите значение издержек\n")
    if costs_input.isdecimal():
        break
    else:
        print("Введено некорректное значение. Повторите ввод")

revenue = int(revenue_input)
costs = int(costs_input)
if revenue > costs:
    profitability = round(((revenue - costs) / revenue) * 100, 2)
    print(f"Компания работает с прибылью. Рентабельность {profitability}%\n")
    while True:
        employee_num_input = input("Введите количество сотрудников компании\n")
        if employee_num_input.isdecimal() and not int(employee_num_input) == 0:
            break
        else:
            print("Введено некорректное значение. Повторите ввод")
    employee_num = int(employee_num_input)
    employee_revenue = round((revenue - costs) / employee_num, 2)
    print(f"Прибыль в расчете на одного сотрудника {employee_revenue}")
else:
    print("Компания убыточна")
