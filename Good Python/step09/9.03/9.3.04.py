def f(a, b):
    if a < 0 and b < 0:
        return "Оба числа отрицательны"
    elif a < 0 or b < 0:
        return "Есть отрицательное число"
    elif a == 0 or b == 0:
        return "Есть 0"
    else:
        return "Оба числа положительны"

print(f(int(input()), int(input())))
