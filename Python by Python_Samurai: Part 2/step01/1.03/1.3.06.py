n = int(input())
for i in range(-n,n+1):
    if i < 0:
        if i % 2 != 0:
            print(f'Число {i} является нечетным и отрицательным')
        else:
            print(f'Число {i} является четным и отрицательным')
    if i >= 0:
        if i % 2 != 0:
            print(f'Число {i} является нечетным и положительным')
        else:
            print(f'Число {i} является четным и положительным')
