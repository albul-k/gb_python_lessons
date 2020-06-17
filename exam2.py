print("""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
""")

list_input = []
while True:
    var_input = input(
        'Введите произвольное значение. (Для завершения введите слово end)\n')
    if not var_input == "":
        if var_input == "end":
            break
        list_input.append(var_input)
    else:
        print('Введено пустое значение. Повторите ввод\n')

print(f"Введенные значения: {list_input}")

list_sorted = []
for i in range(0, len(list_input)):
    if (i % 2 == 0):
        list_sorted.append(list_input[i])
    else:
        list_sorted.insert(i-1, list_input[i])

print(f"Результат сортировки: {list_sorted}")
