n = int(input())
for _ in range(n):
    line = input()
    if not any(c.isupper() for c in line) and any(c.islower() for c in line):
        print(line)
