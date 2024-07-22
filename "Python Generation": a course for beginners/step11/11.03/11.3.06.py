res = []
for _ in range(int(input())):
    res.append(int(input()))
res1 = []
for i in range(len(res)-1):
    res1.append(res[i]+res[i+1])
print(res1)
