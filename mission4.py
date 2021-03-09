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
        return f'{self.name} повернул на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - нормальная скорость.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(TownCar):
    max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


largus = TownCar(60, 'Голубой', 'Ларгус', False)
mark2 = SportCar(130, 'Красная', 'Креста', False)
willis = WorkCar(50, 'Хаки', 'Виллис', False)
lada2115 = PoliceCar(80, 'Белая', 'Чепырка', True)
print(largus.show_speed())
print(willis.show_speed())
print(f'Марка: {lada2115.name}, цвет: {lada2115.color}')
print(f'{lada2115.name} - Полиция? {lada2115.is_police}')
print(f'{mark2.name} - это Полиция? {mark2.is_police}')
print(f'{willis.turn_left()}, а {largus.turn_right()}')