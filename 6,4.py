def schastliviy_bilet(nomer):
    dlina = len(nomer)
    polovina = dlina // 2

    summa1 = 0
    for i in range(polovina):
        summa1 = summa1 + int(nomer[i])

    summa2 = 0
    for i in range(polovina, dlina):
        summa2 = summa2 + int(nomer[i])

    if summa1 == summa2:
        return True
    else:
        return False
nomer = input("Введите номер билета (четное количество цифр): ")
if len(nomer) % 2 != 0:
    print("Ошибка! Количество цифр должно быть четным")
else:
    if schastliviy_bilet(nomer):
        print("Счастливый билет!")
    else:
        print("Обычный билет")