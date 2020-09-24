# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police,direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print(f'{self.name} поехала' )

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула на {self.direction}')

    def police_alarm(self):
        if self.is_police:
            print('прибавьте педальку газа, погоня на хвосте')

    def show_speed(self):
        print(f'Скорость авто {self.name} = {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police,direction):
        super().__init__(speed, color, name, is_police,direction)
    def show_speed(self):
        print(f'Скорость авто {self.name} = {self.speed} км/ч')
        if self.speed > 60:
            print(f'авто {self.name} превысило скорость на {self.speed-60 } км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police,direction):
        super().__init__(speed, color, name, is_police,direction)

class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость авто {self.name} = {self.speed} км/ч')
        if self.speed > 40:
            print(f'авто {self.name} превысило скорость на {self.speed - 40} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police,direction):
        super().__init__(speed, color, name, is_police,direction)


def out_print_info(x):
    print(x.__dict__)
    x.go()
    x.stop()
    x.turn()
    x.show_speed()
    x.police_alarm()


mobile_1 = SportCar(75,'черный','Hyundai',True,"направо")
out_print_info(mobile_1)

mobile_2= WorkCar(45,'белый','Honda',False,"налево")
out_print_info(mobile_2)

mobile_3= PoliceCar(105,'зеленый','Mercedes',True,"направо")
out_print_info(mobile_3)

mobile_4= TownCar(145,'синий','Renault',True,"налево")
out_print_info(mobile_4)