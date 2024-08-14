def find_all(target, symbol):
    res = []
    for i in range(len(target)):
        if target[i] == symbol:
            res.append(i)
    print(res)

target = input()
symbol = input()

find_all(target, symbol)
