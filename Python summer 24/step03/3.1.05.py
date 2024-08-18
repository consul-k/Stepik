n = int(input())
s = 1
while s <= n:
    s+=1
    if n%s == 0:
        print(s)
        break
