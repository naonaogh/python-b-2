text = input('Введите текст: ')
glasny = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы', 'А', 'Я', 'У', 'Ю', 'О', 'Е', 'Ё', 'Э', 'И', 'Ы']
newList = [x for x in text if x in glasny]

print(f'Список гласных букв: {newList}')
print(f'Длина списка: {len(newList)}')