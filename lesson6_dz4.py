class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше чем допустимая для городского транспорта'
        else:
            return f'Скорость {self.name} допустимая для городского транспорта'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость спецтранспорта {self.name} {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше чем допустимая для спецтранспорта'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


audi = SportCar(100, 'Красная', 'Audi', False)
oka = TownCar(30, 'Белая', 'Oka', False)
lada = WorkCar(70, 'Чёрная', 'Lada', True)
ford = PoliceCar(110, 'Синяя',  'Toyota', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} и {lada.show_speed()}')
print(f'{lada.name} {lada.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{lada.name} полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
