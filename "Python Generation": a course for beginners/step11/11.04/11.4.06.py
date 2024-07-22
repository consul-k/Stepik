res = []
for _ in range(int(input())):
    res.append(input())

new = []
for _ in range(int(input())):
    new.append(input())
for i in res:
    if all(a.lower() in i.lower() for a in new):
        print(i)
