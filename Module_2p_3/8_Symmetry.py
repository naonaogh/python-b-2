numberss = int(input('Количество чисел: '))
mass = []
for _ in range(numberss):
    number = int(input('Число: '))
    mass.append(number)

for i in range(len(mass)):
    if mass[i:] == mass[i:][::-1]:
        print('Последовательность: ', mass)
        print("Нужно приписать чисел: ",i)
        print('Сами числа: ',mass[:i][::-1])

        break
