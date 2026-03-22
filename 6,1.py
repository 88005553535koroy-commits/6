def a(chislo):
    if chislo % 3 == 0:
        return True
    else:
        return False
chislo = int(input("Введите число: "))
if a(chislo):
    print("Число делится на 3")
else:
    print("Число не делится на 3")