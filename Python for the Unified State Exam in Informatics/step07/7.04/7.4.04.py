n = int(input())
a = [input() for _ in range(n)]
a = [j for j in a if len(j) > 6]  
print(*a)
