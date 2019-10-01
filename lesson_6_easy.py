class Car:
    def __init__(self, car_name, car_color, car_speed, is_police):
        self.name = car_name
        self.color = car_color
        self.speed = car_speed
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass
