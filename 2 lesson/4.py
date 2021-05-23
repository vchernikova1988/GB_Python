list = input('Enter a word separated by a space: ').split(' ')
for i, v in enumerate(list, 1):
    print(i, v[:10])