def evro(rub):
    return rub / 75.1
def ru(rub):
    return rub / 1
def usa(rub):
    return rub / 66.21
def canada(rub):
    return rub / 50.01
def india(rub):
    return rub / 0.94
def china(rub):
    return rub / 9.53
def jap(rub):
    return rub / 0.59
def uk(rub):
    return rub / 84.9
def oae(rub):
    return rub / 18.03

def main():
    rub = float(input('Введите сумму, которая у вас есть: '))
    strana = input('В какой вы стране: Европа, Россия, США, Канада, Индия, Китай, Япония, Британия, ОАЭ? : ')
    cost = float(input('Введите цену вещи: '))
    if strana == "Европа":
        if evro(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Россия":
        if ru(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "США":
        if usa(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Канада":
        if canada(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Индия":
        if india(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Китай":
        if china(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Япония":
        if jap(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "Британия":
        if uk(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
    elif strana == "ОАЭ":
        if oae(rub) >= cost:
            print('Вы сможите купить эту вещь.')
        else:
            print('У вас недостаточно денег.')
if __name__ == '__main__':
        main()