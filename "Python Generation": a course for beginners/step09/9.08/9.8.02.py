lines = []

while True:
    line = input()
    if line == "КОНЕЦ":
        break
    lines.append(line)

if lines:
    min_line = min(lines)
    max_line = max(lines)
    
    print(f"Минимальная строка ⬇️: {min_line}")
    print(f"Максимальная строка ⬆️: {max_line}")
