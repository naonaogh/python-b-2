guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    leng = len(guests)
    print(f"\nСейчас на вечеринке {leng} гостей: {guests}")
    tut = input("Гость пришел или ушел? ")
    name = input("Имя гостя: ")
    if tut == "пришел":
        if 0 <= len(guests) < 6:
            print(f"Привет, {name}!")
            guests.append(name)
        else:
            print(f"Прости, {name}, но мест нет.")
    elif tut == "ушел":
        print(f"Пока, {name}!")
        guests.remove(name)
    elif tut == "пора спать":
        print("Вечеринка закончелась, все легли спать")
        break
    else:
        print("Вы ввели слово с ошибкой")



