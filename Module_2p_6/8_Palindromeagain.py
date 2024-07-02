stroka = input('Введите строку: ')

def palin(stroka):
    if stroka == stroka[::-1]:
        return True

def palin_dict(stroka):
    dict = {}
    dict[stroka] = stroka[::-1]
    if stroka == stroka[::-1]:
        return True



if palin(stroka):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

if palin_dict(stroka):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')