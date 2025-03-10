s = input()
s1 = set(s)
for i in s:
    if i in s1:
        print(i,end='')
        s1.discard(i)
