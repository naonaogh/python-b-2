passInput = input('Придумайте пароль: ')
if len(passInput) >= 8:
    sumUp = sum(1 if i.istitle() else 0 for i in passInput)
    sumDid = sum(1 if j.isdigit() else 0 for j in passInput)
    if (sumUp >= 1) and (sumDid >= 3):
        print('Это надёжный пароль.')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
else:
    print('Пароль ненадёжный. Попробуйте ещё раз.')