a = list(map(int, input().split()))
for i, v in enumerate(a):
    print(f'индекс {i}, значение {v}')
    a[i] *= 2
    
print(a)
