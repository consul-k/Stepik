import math
n=int(input())
for i in range(n):
    fam=input()
    sum=0
    for x in range(4):
        z=int(input())
        sum+=z
    g=sum*10/4
    if g%10<5:
        sr=int(sum/4)
    else:
        sr=math.ceil(sum/4)
    print(fam,"-",sr)
