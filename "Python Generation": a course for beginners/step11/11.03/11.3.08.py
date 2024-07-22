res = []
for _ in range(int(input())):
    res.append(input())

new = []
c = int(input())
for word in res:
    if len(word) >= c:
        new.append(word[c-1])
print(''.join(new))
