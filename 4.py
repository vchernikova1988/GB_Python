class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started!'

    def stop(self):
        return f'{self.name} is stopped!'

    def turn(self, direction):
        return f'{self.name} turned to ' + direction

    def show_speed(self):
        return f'Current vehicle speed is {self.speed}'

    def police(self):
        if self.is_police == True:
            return f'{self.name} is police'
        elif self.is_police == False:
            return f'{self.name} is not police'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Over speed!'
        else:
            return f'Current vehicle speed is {self.speed}'


class SportCar(Car):
    pass
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Over speed!'
        else:
            return f'Current vehicle speed is {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t = TownCar(100, 'red', 'audi', True)
print(t.show_speed())
print(t.stop())
s = WorkCar(65, 'blue', 'volvo', False)
print(s.turn('city'))

