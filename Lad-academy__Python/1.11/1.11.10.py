def find_all(target, symbol):
    res = []
    for i in range(len(target)):
        if target[i] == symbol:
            res.append(i)
    return res

s = input()
char = input()

print(find_all(s, char))
