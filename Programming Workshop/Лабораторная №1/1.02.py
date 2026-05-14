def PatternCount(text, pattern):
    res = 0
    for i in range(len(text)-(len(pattern)-1)):
        if text[i:i+len(pattern)] == pattern:
            res+=1
    return res

text, pattern = input(), input()
print(PatternCount(text, pattern))
