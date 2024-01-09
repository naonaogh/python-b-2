text = input('Введите строку: ')
result = ''
for item in list(dict.fromkeys(text)):
    count = text.count(item)
    result += f'{item}{count}'
print("Повторяющиеся элементы и их количество: ", result)