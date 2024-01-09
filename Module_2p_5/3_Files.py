name = input('Название файла: ')
mass = ['@', '№', '$', '%', '^', '&', '*', '()']
if name.endswith('.txt') or name.endswith('.docx'):
    for _ in name:
        if _ in mass:
            print('Ошибка: название начинается недопустимым символом.')
            break
        if not _ in mass:
            print('Файл назван верно.')
            break
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')

