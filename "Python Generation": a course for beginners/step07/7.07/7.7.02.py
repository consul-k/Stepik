mx = []
for i in range(10):
    x = int(input())
    if x < 0:
        mx.append(x)

if mx:
    print(sum(mx))
    print(max(mx))
else:
    print("NO")
