"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fibo_gen(). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
"""

from math import factorial


def fibo_gen(n):
    for el in range(1, n + 1):
        yield el


def my_factorial(num: int) -> int:
    fact = 1
    for el in fibo_gen(num):
        fact *= el
    return fact


if __name__ == '__main__':
    assert my_factorial(15) == factorial(15), 'my_factorial(15)'
    print(my_factorial(15))
