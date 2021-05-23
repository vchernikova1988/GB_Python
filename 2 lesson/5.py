my_list = [7, 5, 3, 3, 2]
new_el = int(input('Enter the number: '))
if new_el > len(my_list):
    my_list.insert(0, new_el)
elif new_el < len(my_list):
    my_list.insert(-1, new_el)
else:
    my_list.append(new_el)
print(my_list)

# это задание так и не смогла реализовать до конца, не получается с 1, 4, 5 и 6

