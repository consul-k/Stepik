s = []
for i in data:
    if type(i) == int or type(i) == float:
        s.append(i)
print(sum(s))
