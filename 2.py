class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def __add__(self, other):
        return self.size + other.size, self.height + other.height

    @property
    def my_method(self):
        return f'Размер и рост: {self.size}, {self.height}'

class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def size_coat(self):
        return round(self.size / 6.5 + 0.5)

class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def height_suit(self):
        return round(self.height * 2 + 0.3)

c = Coat(44, 164)
s = Suit(44, 164)
cl = Clothes(44, 164)
print(c.size_coat())
print(s.height_suit())
print(c + s)
print(cl.my_method)





