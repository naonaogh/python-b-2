spisokNachal  = [1, 2, 3, 4, 5]
cdvig = int(input('Сдвиг: '))
while cdvig <= len(spisokNachal):
    n = spisokNachal[-cdvig:] + spisokNachal[:-cdvig]
    break

print(n)