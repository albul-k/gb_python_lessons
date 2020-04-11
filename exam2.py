print("""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
""")

while True:
    i_max = input('Введите количество элементов списка\n')
    if i_max.isdigit():
        break
    else:
        print('Введено некорректное значение. Повторите ввод\n')

list_input = []
while True:
    var_input = input(f'Введите значение {len(list_input)+1} из ({i_max})\n')
    if not var_input == "":
        list_input.append(var_input)
        if len(list_input) == int(i_max):
            break
    else:
        print('Введено пустое значение. Повторите ввод\n')

list_sorted = []
for i in range(0, len(list_input)):
    if (i % 2 == 0):
        list_sorted.append(list_input[i])
    else:
        list_sorted.insert(i-1, list_input[i])

print(f"Результат сортировки: {list_sorted}")
