print("""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
""")

properties = {
    0: 'название',
    1: 'цена',
    2: 'количество',
    3: 'ед'
}

l_prop = []
i = 1
while True:
    print(f'Введите характеристики товара №{i}')
    l = []
    for key, value in properties.items():
        tmp = input(f'{value}\n')
        if not tmp == "":
            l.append(tmp)
        else:
            print('Введено пустое значение. Повторите ввод\n')
            continue
    l_prop.append(l)
    i += 1
    a = input('Ввести характеристики еще одного товара y/n\n')
    if a == "y":
        continue
    else:
        break

products = [
    (ind_prod, {properties[key_prop]:prop for key_prop, prop in enumerate(prod)}) for ind_prod, prod in enumerate(l_prop)
]
print(products)
