a = int(input('Введите результат в первый день в км: '))
b = int(input('Введите желаемый результат в км: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print('Достигнете результата на', i, 'день')
