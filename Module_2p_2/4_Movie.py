films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
wish = []
kolFilm = int(input('Сколько фильмов хотите добавить? '))
for _ in range(kolFilm):
    filmName = input('Введите название фильма: ')
    if filmName in films:
        wish.append(filmName)
    else:
        print('Ошибка: фильма', filmName, 'у нас нет :(')

print('Ваш список любимых фильмов: ', ",".join(wish))