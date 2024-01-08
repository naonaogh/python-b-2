stroka = input('Введите строку: ')
print('Развёрнутая последовательность между первым и последним h:',stroka[stroka.index('h')+1:stroka.rindex('h')][::-1])

