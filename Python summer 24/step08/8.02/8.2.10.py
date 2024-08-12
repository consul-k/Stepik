res = set()
for _ in range(int(input())):
    res.update(set(input().lower()))
print(len(res))
