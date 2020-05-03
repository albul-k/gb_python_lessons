"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


def my_division(x: int, y: int):
    if y == 0:
        raise MyError("Делить на ноль запрещено!")
    return x / y


if __name__ == "__main__":
    print('Операция деления x/y')
    try:
        x = input("Введите число x: \n")
        x = int(x)
        y = input("Введите число y: \n")
        y = int(y)
        print(my_division(x, y))
    except ValueError:
        print('Введено некорректное значение')
