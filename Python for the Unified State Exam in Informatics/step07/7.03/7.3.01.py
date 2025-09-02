b = []
for i in range(7):
    a = int(input())
    b.append(a)

b.sort(reverse=True)

top_4 = b[:4]

m = sum(top_4)

print(m)
