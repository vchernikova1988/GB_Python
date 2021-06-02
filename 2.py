f = open('2.txt', 'r')
content = f.readlines()
print(content)
print(f'Количество строк: {len(content)}')
for line in content:
    print(f'Количество слов: {len(line.split())}')
f.close()