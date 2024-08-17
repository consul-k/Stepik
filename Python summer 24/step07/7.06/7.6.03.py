def numbers(n):
    res = ''
    for i in range(1,n+1):
        res += str(i)*i
    return res

print(numbers(int(input())))
