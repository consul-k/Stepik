nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested_list:
    for j in range(len(i)):
        if i[j]%2!=0:
            i[j] = 0
print(nested_list)
