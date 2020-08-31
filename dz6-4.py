#dz6-4

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} start'

    def stop(self):
        return f'{self.name} stop'

    def turn_right(self):
        return f'{self.name} turn right'

    def turn_left(self):
        return f'{self.name} turn left'

    def show_speed(self):
        return f'speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is high'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is high'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is the police'
        else:
            return f'{self.name} is not the police'


bmw = SportCar(150, 'Black', 'BMW', False)
mini = TownCar(60, 'White', 'MINI', False)
audi = WorkCar(100, 'Red', 'AUDI', True)
ford = PoliceCar(150, 'Green',  'FORD', True)
print(audi.turn_left())
print(f'When {mini.turn_right()}, then {bmw.stop()}')
print(f'{audi.go()} speed {audi.show_speed()}')
print(f'{audi.name} is {audi.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {audi.name}  a police car? {audi.is_police}')
print(bmw.show_speed())
print(mini.show_speed())
print(ford.police())
print(ford.show_speed())