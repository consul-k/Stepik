def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sf(n):
    if n == 0 or n == 1:
        return 1
    else:
        sf = 1
        for i in range(1, n+1):
            sf *= factorial(i)
        return sf
