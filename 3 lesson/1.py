#1
def division(ar1, ar2):
    try:
        res = ar1 // ar2
        return(res)
    except ValueError:
        return('No!')
    except ZeroDivisionError:
        print('Error!!!')
        return('Try again!')

print(division(int(input('ar1: ')), int(input('ar2: '))))

#2
def division(ar1, ar2):
    if ar2 == 0:
        print('Делитель равен нулю!')
        return('Попробуй еще раз!')
    else:
        res = ar1 // ar2
        return (res)

print(division(int(input('ar1: ')), int(input('ar2: '))))
