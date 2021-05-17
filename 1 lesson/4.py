num = int(input('Введите целое положительное число: '))
i = num % 10
num = num // 10
while num > 0:
    if num % 10 > i:
        i = num % 10
    num = num // 10
print(i)