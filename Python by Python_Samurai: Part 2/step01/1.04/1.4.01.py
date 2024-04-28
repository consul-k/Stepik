a = input().split()
a = list(enumerate(a))
print(*list(i[1] for i in a if i[0]%2!=0))
