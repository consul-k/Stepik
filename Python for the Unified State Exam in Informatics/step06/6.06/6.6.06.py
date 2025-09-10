max=-1
for n in range(3,1000):
    a = '9' + n * '3'
    while '22' in a or '333' in a or '9999' in a:
        if '22' in a:
            a=a.replace('22','3',1)
        if '333' in a:
            a=a.replace('333','99',1)
        if '9999' in a:
            a=a.replace('9999','22',1)
    y=1
    for s in a:
            y*=int(s)
            if y>max:
                max=y
print(max)
