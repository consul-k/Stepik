a = list(map(int, input().split()))
n = int(input())
for i in range(len(a)):
    if a[i] == n:
        print(i+1)
if n not in a:
    print(f'Число {n} отсутствует в списке {a}')
