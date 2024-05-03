# продолжите решение здесь
lst = list(map(int, input().split()))
for i in lst:
    match i:
        case 1:
            print('найдено число 1')
        case 9:
            print('найдено число 9')
        case _:
            print('нужные числа не найдены')
