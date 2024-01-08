mass1 = [(1 if x == 0 or x % 2 == 0 else x % 5)
         for x in range(0, int(input('Введите длину списка: '))) ]
print(mass1)