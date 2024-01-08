kolich = int(input('Количество видеокарт: '))
obsh = []
new = []
stariy = []
count = 1
for _ in range(kolich):
    card = int(input('Видеокарта ' + str(count) + ": " ))
    count += 1
    obsh.append(card)

print('Старый список видеокарт: ', obsh)

stariy = max(obsh)
new = [i for i in obsh if i != stariy]
print('Новый список видеокарт: ', new)