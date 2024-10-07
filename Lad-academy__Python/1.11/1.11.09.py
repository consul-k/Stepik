def get_factors(num):
    res = [1]
    for i in range(2,num+1):
        if num%i==0:
            res.append(i)
    return res

n = int(input())

print(get_factors(n))
