s = input()
result = dict(zip([i for i in s.split()], [s.count(i) for i in s.split()]))
m = max(result.values())
list_m = []

for word in result:
    if result[word] == m:
        list_m.append(word)
        
list_m = sorted(list_m)

print(list_m[0])
