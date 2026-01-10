n = int(input())

rappers = []

for _ in range(n):
    line = input().strip()
    parts = line.split()
    score = int(parts[-1])
    name = ' '.join(parts[:-1])
    rappers.append((name, score))

rappers.sort(key=lambda x: x[1], reverse=True)

print(rappers[:3])
