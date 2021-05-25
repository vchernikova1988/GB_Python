def my_func(a, b, c):
   inf = [a, b, c]
   return sum(sorted(inf)[-2:])

print(my_func(1, 2, 3))