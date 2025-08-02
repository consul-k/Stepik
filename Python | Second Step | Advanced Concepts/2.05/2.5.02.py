nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [j for i in nested_list for j in i if j%2==0]
print(res)
