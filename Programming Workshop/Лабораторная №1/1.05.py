def PatternMatching(text, pattern):
    res = []
    for i in range(len(text)):
        if text.find(pattern, i) != -1 and text.find(pattern, i) not in res:
            res.append(text.find(pattern, i))
    return res

pattern, text = input(), input()
print(*PatternMatching(text, pattern))
