def get_last_index(data, value):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i
    return "ERROR!"

data = eval(input())
value = eval(input())

print(get_last_index(data, value))
