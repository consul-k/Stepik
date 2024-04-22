a = list(map(int, input().split()))
n = int(input())
if n in a:
    print(f'Число {n} присутствует в списке {a}.')
else:
    print(f'Число {n} отсутствует в списке {a}.')
