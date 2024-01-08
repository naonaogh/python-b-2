kolRoll = int(input('Количество роликов: '))
numb1 = 1
massRoll = []
for i in range(kolRoll):
    razmerRoll = int(input(f'Размер пары {numb1}: '))
    numb1 += 1
    massRoll.append(razmerRoll)

kolPolz = int(input('Количество людей: '))
numb2 = 1
massPolz = []
for i in range(kolPolz):
    razmerPolz = int(input(f'Размер ноги человека {numb2}: '))
    numb2 += 1
    massPolz.append(razmerPolz)

ispolz = 0
for j in massRoll:
    for h in massPolz:
        if j == h:
            ispolz += 1

print(f'Наибольшее количество людей, которые могут взять ролики: {ispolz}')