res = 0
for i in range(1, int(input())):
    if i%5==0 or i%3==0:
        res+=i
print(res)
