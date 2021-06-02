try:
    with open('5.txt', 'w+') as f:
        content = input('Enter numbers separated by a space: ').split()
        f.write(str(content) + '\n')
        a = 0
        for line in content:
            a += int(line)
            print(a)
except IOError:
    print('An I / O error has occurred!')
except ValueError:
    print('Wrong number dialed. I / O error')
