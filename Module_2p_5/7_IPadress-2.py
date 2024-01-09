ipAdress = input('Введите IP: ').split('.')
for i in ipAdress:
    if len(ipAdress) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    if not i.isdigit():
        print(f'{i} - это не целое число.')
        break
    if (int(i) > 255):
        print(f'{i} превышает 255.')
        break
else:
    print('IP-адрес корректен')
