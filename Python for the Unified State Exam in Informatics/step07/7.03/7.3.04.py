a = input()
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
b.remove(max(b))
b.remove(min(b))
m = sum(b)/len(b)
print(m)
