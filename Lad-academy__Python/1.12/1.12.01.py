def is_prime(num):
    res = [1]
    for i in range(2,num+1):
        if num%i==0:
            res.append(i)
    if len(res) == 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))
