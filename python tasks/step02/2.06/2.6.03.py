set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = sorted(set1 & set2)

print(*result)
