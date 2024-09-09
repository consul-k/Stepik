a = input()
res = ''
for i in range(len(a)):
    if i%3!=0:
        res += a[i]
print(res)
