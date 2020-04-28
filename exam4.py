"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    _direction = ''

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'машина {self.name} поехала'

    def stop(self):
        return f'машина {self.name} остановилась'

    def turn(self, direction):
        self._direction = direction
        if self._direction == 'left':
            return f'машина {self.name} повернула налево'
        else:
            return f'машина {self.name} повернула направо'

    def show_speed(self, speed):
        self.speed = speed
        return self.speed


class TownCar(Car):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            return 'превышение разрешенной скорости'
        else:
            return speed


class SportCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            return 'превышение разрешенной скорости'
        else:
            return speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True
        super().__init__(speed, color, name, self.is_police)


if __name__ == '__main__':
    town_car = TownCar(speed=50, color='white', name='Ford Focus')
    print('TownCar')
    print(town_car.go())
    print(town_car.stop())
    print(town_car.turn('left'))
    print(town_car.show_speed(55))
    print(town_car.show_speed(65))

    sport_car = SportCar(speed=100, color='red', name='Ford Mustang')
    print('=============')
    print('SportCar')
    print(sport_car.go())
    print(sport_car.stop())
    print(sport_car.turn('right'))
    print(sport_car.show_speed(200))

    work_car = WorkCar(speed=30, color='green', name='Ford Fiesta')
    print('=============')
    print('WorkCar')
    print(work_car.go())
    print(work_car.stop())
    print(work_car.turn('left'))
    print(work_car.show_speed(40))
    print(work_car.show_speed(50))

    police_car = PoliceCar(speed=80, color='blue', name='Ford Explorer')
    print('=============')
    print('PoliceCar')
    print(police_car.go())
    print(police_car.stop())
    print(police_car.turn('right'))
    print(police_car.show_speed(100))
