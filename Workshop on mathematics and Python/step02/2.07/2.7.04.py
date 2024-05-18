def Kfactorial(n, k=1):
    result = 1
    for i in range(n, 0, -k):
        result *= i
    return result
