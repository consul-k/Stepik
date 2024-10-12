def sum_range(start, end):
    res = 0
    if start < end:
        for i in range(start, end+1):
            res += i
        return res
    else:
        for i in range(end, start+1):
            res += i
        return res

data = list(map(int, input().split()))
print(sum_range(data[0], data[1]))
