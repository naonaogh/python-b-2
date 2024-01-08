violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]]
kolPesen = int(input('Сколько песен выбрать? '))
newPlaylist = []
dlina = 0

for i in range(kolPesen):
    nazva = input(f'Название {i+1}-й песни: ')
    newPlaylist.append(nazva)
for j in violator_songs:
    if j[0] in newPlaylist:
        dlina += j[1]

print(f'Общее время звучания песен - {round(dlina, 2)}')