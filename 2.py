class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class Patern(Road):
    def __init__(self, _length, _width, distance):
        super().__init__(_length, _width)
        self.distance = distance

a = Patern(20, 5000, 25)
print(a.mass())
