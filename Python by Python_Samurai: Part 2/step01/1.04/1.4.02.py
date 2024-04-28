a = input().split()
new_lst = []
for i, v in enumerate(a, start=1):
    new_lst.append([v,i])
print(new_lst)
