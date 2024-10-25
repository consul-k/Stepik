n = int(input())
cnt = 0
for i in numbers:
    if i > n:
        cnt += 1
print(f'Количество элементов больше {n}: {cnt}')
