filename = input().strip()

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())

print(len(lines))
