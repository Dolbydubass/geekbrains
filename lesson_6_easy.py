class Car:
    def __init__(self, car_name, car_color, car_speed, is_police: bool):
        self.name = car_name
        self.color = car_color
        self.speed = car_speed
        self.is_police = bool(is_police)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def __init__(self, car_name, car_color, car_speed, is_police: bool):
        super().__init__(car_name, car_color, car_speed, is_police=False)


class SportCar(TownCar):
    pass


class WorkCar(TownCar):
    pass


class PoliceCar(Car):
    def __init__(self, car_name, car_color, car_speed, is_police: bool):
        super().__init__(car_name, car_color, car_speed, is_police=True)


# Тест:
prius = TownCar('Prius', 'Белый', '60 км/ч', '')
prius.go()
print(prius.name)
print(prius.color)
print(prius.speed)
print(prius.is_police)
print()
mercedes = SportCar('Mercedes', 'Черный', '210 км/ч', '')
mercedes.stop()
print(mercedes.name)
print(mercedes.color)
print(mercedes.speed)
print(mercedes.is_police)
print()
solaris = TownCar('Solaris', 'Синий', '60 км/ч', '')
solaris.go()
print(solaris.name)
print(solaris.color)
print(solaris.speed)
print(solaris.is_police)
print()
ford = PoliceCar('Ford', 'LAPD', '110 км/ч', '')
ford.turn('налево')
print(ford.name)
print(ford.color)
print(ford.speed)
print(ford.is_police)
