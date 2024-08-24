res = []
for _ in range(int(input())):
    res.append(input())

s = input()

for i in res:
    if s.lower() in i.lower():
        print(i)
