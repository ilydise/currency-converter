x = input('Enter the amount of currency and the currency itself (or name) to convert:')


def is_number(x):
    y = ''
    p = ''
    for i in x:
        try:
            int(i)
            y = y + i
        except ValueError:
            p = p + i
    return y, p


quantity, valut = map(str, is_number(x))
quantity = int(quantity)


def convertor(qauntity, valut):
    if valut == '$' or 'dol' in valut:
        print(f'{int(qauntity * 75.47)} rub\n'
              f'{int(qauntity * 0.94)} euros')
    elif 'EU' or 'eu' in valut:
        if quantity < 2:
            dol = 'dollar'
        elif quantity >= 2:
            dol = 'dollars'
        print(f'{int(qauntity * 80.19)} rub\n'
              f'{int(qauntity * 1.06)} {dol}')
    elif 'RU' or 'ru' in valut:
        if quantity <= 75:
            dol1 = 'dollar'
        elif 75 < quantity < 375:
            dol1 = 'dollar'
        elif quantity >= 375:
            dol1 = 'dollars'
        print(f'{(qauntity * 0.01325)} {dol1}\n'
              f'{(qauntity * 0.01247)} euro')


print(quantity, valut)
convertor(quantity, valut)