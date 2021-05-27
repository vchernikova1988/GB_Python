from sys import argv

hours, hour, pay = map(int, argv[1:])

formula = hours * hour + pay

print(f'Your pay is {formula}')
