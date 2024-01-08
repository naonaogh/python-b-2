spisok = int(input('Введите колчество значений в списке: '))
mass = []
for _ in range(spisok):
    number = int(input('Введите значение: '))
    mass.append(number)
print(mass)

i = 0
while i < len(mass):
    if mass[i] % 2 != 0:
        del mass[i]
    else:
        i+=1


for i in range(len(mass)):
    for j in range(len(mass)-1):
        if mass[j] < mass[j+1]:
            mass[j], mass[j+1] = mass[j+1], mass[j]


print(mass)