def alphabet():
    a = ord('а')
    A = ord('А')
    mass = []
    list1 = ''.join([chr(i) for i in range(a, a + 32)])
    list2 = ''.join(chr(i) for i in range(A, A + 32))
    mass.extend(list1)
    mass.extend(list2)
    return mass

def shifr(text, symbols, n):
    index = symbols.index(text)
    if index + n >= 0:
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]

def result(text, n):
    res = ""

    for i in range(0, len(text)):
        if text[i] in abc:
            res += shifr(text[i], abc, sdvig)
        else:
            res += text[i]

    return res

text = input('Введите сообщение: ')
sdvig = int(input('Введите сдвиг: '))
abc = alphabet()
print(abc)
print(result(text, sdvig))