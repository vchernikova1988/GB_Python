proceeds = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))
if proceeds > cost:
    profit = proceeds - cost
    print('Ваша прибыль: ', profit)
    profitability = (profit / proceeds) * 100
    print('Рентабельность выручки: ', '%d' % profitability)
    stuff = int(input('Введите число сотрудников: '))
    stufit = profit // stuff
    print('Прибыль в расчете на одного сотрудника: ', stufit)
elif proceeds < cost:
    lesion = cost - proceeds
    print('Ваш убыток: ', lesion)
elif proceeds == cost:
    print('Выручка равна издержкам')
else:
    print('Невозможно отобразить данные')

