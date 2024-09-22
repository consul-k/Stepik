text = input().split()
d = {}
result = []
for symb in text:
    d[symb] = d.get(symb, -1) + 1
    if d[symb] > 0:
        print(symb+'_'+str(d[symb]), end = ' ')
    else:
        print(symb, end = ' ')
