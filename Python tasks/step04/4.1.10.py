lst = []
i = int(input())
while i != -1:
    lst.append(i)
    i = int(input())
lst = [i for i in lst if i%2==0]
print(sorted(lst))
