stop = True
sum = 0
while stop:
    user_list = (input('Enter numbers: ')).split()
    sum_part = 0
    for el in user_list:
        if el == '$':
            stop = False
            break
        else:
            sum_part += int(el)
    sum += sum_part
    print(sum)


