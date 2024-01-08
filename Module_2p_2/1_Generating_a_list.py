your_number = int(input('Введите число: '))
spisok = []
for i in range(your_number):
    if i % 2 != 0:
        spisok.append(i)

print('Список из нечётных чисел от одного до N: ', spisok)