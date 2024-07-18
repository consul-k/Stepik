a = input()
a1 = a[:len(a)-len(a)//2]
a2 = a[len(a)-len(a)//2:len(a)]
print(a2+a1)
