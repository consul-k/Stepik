d = {}
lst = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in lst:
    d[word] = d.get(word, 0) + 1
lst = [(value, key) for key, value in d.items()]
lst.sort()
print(lst[0][1])
