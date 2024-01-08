while True:
    passInput = input('Придумайте пароль: ')
    if len(passInput) >= 8:
        sumUp = sum(1 for i in passInput if i.isupper())
        sumDid = sum(1 for j in passInput if j.isdigit())
        if (sumUp > 1) and (sumDid >= 3):
            print('Это надёжный пароль.')
            break
    print('Пароль ненадёжный. Попробуйте ещё раз.')
