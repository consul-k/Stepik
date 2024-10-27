a = int(input())
b = int(input())
if a > b:
    while a >= b:
        print(a)
        a-=1
else:
    while b >= a:
        print(b)
        b-=1
