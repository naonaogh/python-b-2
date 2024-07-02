text = input("Введите текст: ")
diction = {}
for key in text:
    if key in diction:
        diction[key] += 1
    else:
        diction[key] = 1
print(f"Оригинальный словарь частот: {diction}")
new_dict = {}
for kk, vl in diction.items():
    if vl in new_dict:
        new_dict[vl].append(kk)
    else:
        new_dict[vl] = [kk]
print(f"Инвертированный словарь частот: {new_dict}")

