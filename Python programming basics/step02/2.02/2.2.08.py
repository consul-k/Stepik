import math

word = input().split()
res = ''

for i in word:
    i = i.replace(',','').replace('!','')
    res += i[-1]
    if len(i)%2==0:
        res+=i[len(i)//2]
    else:
        res+=i[math.floor(len(i)/2)]
        
print(res)
