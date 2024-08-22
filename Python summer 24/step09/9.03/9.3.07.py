d = {}
for _ in range(int(input())):
    l = input().lower().split()
    if l[1] not in d:
        d[l[1]] = [l[0]]
    else:
        d[l[1]] += [l[0]]
    
for ask in range(int(input())):
    ask = input().lower()
    if ask in d:
        print(*d[ask])
    else:
        print('абонент не найден')
