l = set()
for i in range(int(input())):
    i = set(map(int, input().split()))
    l.update(i)
print(len(l))
