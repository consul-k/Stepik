try:
    a = int(input())
    b = int(input())
    print(a/b)
except ValueError:
    print('Ошибка. Буквы вместо чисел')
except ZeroDivisionError:
    print('Ошибка. Делить на ноль нельзя')
