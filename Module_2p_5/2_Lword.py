text = input('Введите строку: ').split()
count = []
for word in text:
    count.append(len(word))
    maxCount = max(count)

print('Самое длинное слово:', max(text, key=len))
print('Длина этого слова:', maxCount)

