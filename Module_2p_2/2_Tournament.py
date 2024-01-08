spisok_uchast = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя',  'Захар']
spisok_fday = []

spisok_fday.append(spisok_uchast[::2])

print('Первый день:', *spisok_fday)