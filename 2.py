class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    res = num_1 // num_2
except ZeroDivisionError:
    print("На ноль делить нельзя")
except (ValueError, MyError) as err:
    print(err)
else:
    print(res)