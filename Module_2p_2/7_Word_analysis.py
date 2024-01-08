mass = []
slovo = input('Введите слово: ')
for _ in slovo:
    mass.append(_)
if mass == mass[::-1]:
    print('Слово является палиндромом ')
else:
    print('Слово не является палиндромом')