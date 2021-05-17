t = int(input('Enter the time in seconds: '))

print('%02dh:%02dm:%02ds' % (t / 3600, t % 3600 / 60, t % 3600 % 60))
