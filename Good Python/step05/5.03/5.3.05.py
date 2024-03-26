def fact(s):
    f = 1
    for i in range(1,s+1):
        f *= i
    return(f)

n = int(input())
k = int(input())
print(int(fact(n) / (fact(k) * fact(n-k))))
