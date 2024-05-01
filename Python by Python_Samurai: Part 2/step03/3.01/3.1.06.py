words = tuple(input().split())
result = []
for i in range(len(words)):
    if words.count(words[i]) > 1 and i not in result:
        result.append(i)
print(*result)
