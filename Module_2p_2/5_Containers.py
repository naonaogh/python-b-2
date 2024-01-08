containers = []
kolvo = int(input('Количество контейнеров: '))
for _ in range(kolvo):
    ves = int(input('Введите вес контейнера: '))
    if ves < 200:
        containers.append(ves)
    else:
        print('Превышение веса!')

newCont = int(input('Введите вес нового контейнера: '))
if newCont < 200:
    containers.append(newCont)
else:
    print('Превышение веса!')

containers.sort(reverse=True)
indexx = containers.index(newCont) + 1
print('Номер, который получит новый контейнер: ', indexx)