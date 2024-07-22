res = []
for _ in range(int(input())):
    res.append(input())
new = []
for i in res:
    if i not in new:
        new.append(i)
        print(i)
