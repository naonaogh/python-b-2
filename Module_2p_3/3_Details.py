shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],['педаль', 100],
        ['седло', 1500],  ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
countt = 0
cost = 0
name = input('Введите название детали: ')
for i in shop:
    if i[0] == name:
        countt += 1
        cost += i[1]


print('Введите количество деталей: ', countt)
print('Стоимость деталей: ', cost)

