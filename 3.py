with open('3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key} зарплата меньше 20 тысяч')
        person = 0
        total = 0
        total += int(value)
        person += 1
result = total // person
print(f'Средняя величина дохода сотрудников: {result}')