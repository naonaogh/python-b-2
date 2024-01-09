def count_uppercase_lowercase(text):
    uppercase = sum(i.isupper() for i in text)
    lowercase = sum(i.islower() for i in text)
    return uppercase, lowercase


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)