list_1 = input().split()
list_2 = input().split()

res = set(list_1) ^ set(list_2)
print(sorted(list(res)))
