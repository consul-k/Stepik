identifiers = input().split()

count = {}
result = []

for identifier in identifiers:
    if identifier not in count:
        count[identifier] = 1
        result.append(identifier)
    else:
        result.append(f"{identifier}_{count[identifier]}")
        count[identifier] += 1

print(" ".join(result))
