x = input().split()
if len(x) == 1:
    print(x[0])
elif len(x) > 1:
    y = [int(x[i-1])+int(x[i+1]) for i in range (-1, len(x)-1)]
    for i in range (1, len(y)):
        print(y[i], end=' ')
    print(y[0])
