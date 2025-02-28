s = input().split(',')
a = set()
for i in s:
    if i.lower() in a:
        print('ДА')
    else:
        print('НЕТ')
    a.add(i.lower())
