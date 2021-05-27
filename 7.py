def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x

for el in fact(4):
    print(el)