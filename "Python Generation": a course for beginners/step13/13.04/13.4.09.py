# объявление функции
def find_all(target, symbol):
    res = []
    for i in range(len(target)):
        if target[i] == symbol:
            res.append(i)
    return res

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
