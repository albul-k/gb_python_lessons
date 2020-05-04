"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = ''
    _width = ''

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, mass, heigth):
        return self._length * self._width * mass * heigth


my_road = Road(20, 5000)

if __name__ == '__main__':
    assert my_road.calc_asphalt_mass(
        25, 5) == 12500000, 'my_road.calc_asphalt_mass(25, 5)'
    print(my_road.calc_asphalt_mass(30, 10))
