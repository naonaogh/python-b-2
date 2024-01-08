kolChel = int(input('Количество человек: '))
mesto  = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {mesto}-й человек\n')
krug = [i for i in range(1, kolChel+1)]
start = 0
while len(krug) > 1:
    print(f'Текущий круг людей: {krug}')
    minus = (start + mesto - 1) % len(krug)
    startSchot = start % len(krug)
    print(f'Начало счёта с номера {krug[startSchot]}')
    start = (startSchot + mesto - 1) % len(krug)
    print('Выбывает человек под номером', krug[start])
    krug.remove(krug[start])
    print(end = '\n')
print('Остался человек под номером', *krug)