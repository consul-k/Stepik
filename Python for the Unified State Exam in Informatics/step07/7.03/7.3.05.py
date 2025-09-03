a = input()
b = a.split()
c1 = 0
c2 = 0
pr = 0
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(b)):
    s = min(b)
    if s % 2 == 0:
        c1+=1
        pr+=s
    else:
        c2+=1
        pr+=s
    b.remove(min(b))
    s = 0
if c1 > c2:
    print(f"Михаил {pr}")
elif c1 < c2:
    print(f"Жанна {pr}")
else:
    print(f"Поровну {pr}")
