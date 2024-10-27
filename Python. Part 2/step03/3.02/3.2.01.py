a = int(input())
b = int(input())
if b > a:
    for i in range(a, b+1):
        if i % 3 == 0:
            continue
        print(i)
else:
    for i in range(b, a+1):
        if i % 3 == 0:
            continue
        print(i)
