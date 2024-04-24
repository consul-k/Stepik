a, b = map(int, input().split())
min_num = a if a < b else b
max_num = a if a > b else b
print(min_num, max_num)
