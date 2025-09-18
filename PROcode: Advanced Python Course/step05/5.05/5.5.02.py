s = tuple(map(int, input().split()))
n = int(input())

print(f'Число {n} встречается {s.count(n)} раз(а) в кортеже.')

if n not in s:
    print(f'Число {n} не найдено в кортеже.')
else:
    print(f'Первое вхождение числа {n} находится на индексе {s.index(n)}.')
