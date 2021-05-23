#2 dict
seasons = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
month = int(input('Enter month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print('It is', key, '!')

#2 list
list = ['winter', 'spring', 'summer', 'autumn']
month = int(input('Enter month: '))
if month == 1 or month == 2 or month == 12:
    print(f'It is {list[0]} !')
elif month == 3 or month == 4 or month == 5:
    print(f'It is {list[1]} !')
elif month == 6 or month == 7 or month == 8:
    print(f'It is {list[2]} !')
elif month == 9 or month == 10 or month == 11:
    print(f'It is {list[3]} !')
else:
    print('There is no such month!')





