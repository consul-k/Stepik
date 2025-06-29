a = tuple(input().split())
b = []

for i in a:
    if i not in b:
        b.append(i)
        
print(len(b))
print(a)
