lst = input().split(', ')
a = []
b = []

for i in lst:
    if 'повреждён' in i:
        i = i.replace(' повреждён','')
        b.append(i)
    else:
        a.append(i)
        
print('Целое снаряжение:', list(reversed(a)))
print('Поврежденное снаряжение:', list(reversed(b)))
