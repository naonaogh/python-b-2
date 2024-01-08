a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
c_five = a.count(5)
countf = 0
countt = 0
for _ in a:
    if _ == 5:
        countf += 1
        a.remove(5)
a.extend(c)
for _ in a:
    if _ == 3:
        countt += 1
print('Количество цифр 5 при первом объединении: ', countf)
print('Количество цифр 3 при втором объединении: ', countt)
print('Итоговый список: ', a)
