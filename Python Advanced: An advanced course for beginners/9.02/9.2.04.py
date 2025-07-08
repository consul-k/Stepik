import sys

lst = list(map(str.strip, sys.stdin.readlines()))
candidates = set()

for line in lst:
    if ':' in line:
        name = line.split(':', 1)[0].strip()
        candidates.add(name)

print(len(candidates))
