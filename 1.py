class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'Матрица с параметрами: {self.matrix}'

    def __add__(self, other):
        res = []
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                res.append(self.matrix[x][y] + other.matrix[x][y])
        return Matrix(res)

one = Matrix([[5, 8, 3], [3, 7, 1]])
two = Matrix([[31, 37, 51], [22, 43, 86]])
print(one)
print(two)
three = one + two
print(three)