violator_songs = \
{
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
Sum = 0
Qsong = 0
QuantSong = int(input('Сколько песен выбрать? '))
for i in range(QuantSong):
    Qsong += 1
    NameSong = input(f'Название {Qsong}-й песни: ')
    if NameSong not in violator_songs:
        print('Вы ввели отсутствующую песню ')
        NewName = input('Введите корректное название: ')
        Sum = Sum + violator_songs.get(NewName)
    else:
        Sum = Sum + violator_songs.get(NameSong)


print(f'Общее время звучания песен: {round(Sum,3)}')