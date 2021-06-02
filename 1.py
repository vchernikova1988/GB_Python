with open('first.txt', 'w') as f:
    while True:
        line = input('Enter anything: ')
        if line == '':
            break
        f.write(line + '\n')


