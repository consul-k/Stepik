matrix = [list(map(int, input().split())) for i in range(int(input()))]
test_list = []

for i in range(len(matrix)):
    test_list.extend(matrix[i][:i+1])
    
print(max(test_list))
