numbers = list(map(int, input().split()))
seen = {}
unique = []

for num in numbers:
    if num not in seen:
        seen[num] = True
        unique.append(num)

print(*unique)
