kolvo = int(input("Введите количество заказов: "))
orders = {}

for i in range(kolvo):
    while True:
        char = input(f"Заказ №{i + 1}: ").strip().split(' - ')
        if len(char) == 3:
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите пару слов в формате 'Имя - заказ - количество'.")

    name, zakaz, col = char
    col = int(col)

    if name.lower() not in orders:
        orders[name.lower()] = {}

    if zakaz in orders[name.lower()]:
        orders[name.lower()][zakaz] += col
    else:
        orders[name.lower()][zakaz] = col

print(orders)
