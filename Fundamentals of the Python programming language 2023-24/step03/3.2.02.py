lst1 = []
for i in range(10):
    lst1.append(int(input()))
lst1.sort(reverse=True)
for i in lst1:
    print(i)
