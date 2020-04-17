"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def my_func(arg: str) -> str:
    """Преобразование первой буквы слова к заглавному виду

    Arguments:
        string {str} -- слово

    Returns:
        str -- преобразованное слово
    """
    try:
        return arg.title()
    except ValueError:
        return arg


def conv_string():
    tmp = input('Введите список слов через пробел\n')
    try:
        word_list = tmp.split()
    except ValueError:
        print('')

    word_list_new = []
    for itm in word_list:
        word_list_new.append(my_func(itm))
    return (' ').join(word_list_new)


print(conv_string())
