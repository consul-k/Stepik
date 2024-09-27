matrix = [list(map(int, input().split())) for i in range(int(input()))]

for i in matrix:
    check = 0
    for num in i:
        if num > sum(i) / len(i):
            check+=1
    print(check)
