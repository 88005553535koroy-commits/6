def a(chislo):
    return 100 / chislo
try:
    chislo = int(input("Введите число: "))
    rezultat = a(chislo)
    print("100 /", chislo, "=", rezultat)
except ValueError:
    print("Ошибка! Нужно ввести число, а не текст")
except ZeroDivisionError:
    print("Ошибка! На ноль делить нельзя")
except Exception:
    print("Произошла какая-то другая ошибка")