from string import ascii_uppercase
n = int(input())
a = list(ascii_uppercase[:n])
s = []
for i in range(n):
    s.append(a[i]*(i+1))
print(s)
