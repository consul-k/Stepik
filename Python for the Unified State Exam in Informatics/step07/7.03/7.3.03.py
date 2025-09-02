n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
c=0
for x in range(1000):
    if x in a:
        if a.count(x) > a.count(c):
            c=x
print(c)
