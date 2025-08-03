list_1 = list(input().split()) #создание списка из введённых элементов
res = set([int(i) for i in list_1])
print(sorted(list(res)))
