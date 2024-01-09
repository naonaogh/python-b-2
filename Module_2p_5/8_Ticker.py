str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')

if str1 == str2:
    print('Строчки одинаковы')
elif len(str1) != len(str2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    count = 1
    f = False
    for i in range(len(str2) - 1):
        str2 = str2[-1] + str2[:-1]
        if str1 == str2:
            f = True
            print('Первая строка получается из второй со сдвигом', count)
            break
        else:
            count += 1
    if not f:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
