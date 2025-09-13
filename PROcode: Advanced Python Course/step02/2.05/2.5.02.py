a = input().split(', ')
res = 0
i = 0

while i != len(a):
    if a[i] == 'ignore':
        print(a[i])
        res += 1
    i += 1
print(res)
