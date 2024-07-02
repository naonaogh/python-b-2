numb_pair = int(input('Введите количество пар слов: '))
dict = {}

for i in range(numb_pair):
    pair = input(f"Пара {i + 1}: ").strip().split(' - ')
    if len(pair) != 2:
        print("Некорректный ввод. Пожалуйста, введите пару слов в формате 'слово — синоним'.")
        pair = input(f"Пара {i+1}: ").strip().split(' - ')
    word1, word2 = pair
    dict[word1.lower()] = word2
    dict[word2.lower()] = word1

check = input("Введите слово для проверки: ")
if check not in dict:
    print("Такого слова в словаре нет.")
else:
    print(f"Синоним: {dict[check]}")