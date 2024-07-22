n = int(input().strip('#'))
for _ in range(n):
    line = input()
    if '#' in line:
        line = line[:line.index('#')]
    print(line.rstrip())
