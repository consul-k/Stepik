def FrequentWords(text, k):
    res = {}
    for i in range(len(text)-(k-1)):
        if text[i:i+k] not in res:
            res[(text[i:i+k])] = text.count(text[i:i+k])
    max_value = max(res.values())
    return sorted(key for key in res if res[key] == max_value)

text, k = input(), int(input())
print(*FrequentWords(text, k))
