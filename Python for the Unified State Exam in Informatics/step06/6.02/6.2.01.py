n = int(input())
count = 0

for _ in range(n):
    s = input().strip()
    if s and s[0] == s[-1]:
        count += 1

print(count)
