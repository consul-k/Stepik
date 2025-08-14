s = input()
sub = input()

res = []
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        res.append(i)

if res:
    print(*res)
else:
    print(-1)
