"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class ComplexNum:
    num = 0

    def __init__(self, x: float, y: float) -> float:
        self.num = complex(x, y)

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


if __name__ == "__main__":
    num_1 = ComplexNum(2, 3)
    num_2 = ComplexNum(3, 4)

    assert num_1 + num_2 == (5+7j), 'num_1 + num_2'
    assert num_1 * num_2 == (-6+17j), 'num_1 * num_2'

    print(num_1 + num_2)
    print(num_1 * num_2)
