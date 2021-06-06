class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка: {self.title}'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка: {self.title}'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка: {self.title}'

p = Stationery('предмет')
print(p.draw())
r = Pen('ручка')
print(r.draw())
k = Pencil('карандаш')
print(k.draw())
m = Handle('маркер')
print(m.draw())