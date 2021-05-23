list = input('Enter list items separated by space: ').split(' ')
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
    i += 2
print(list)




