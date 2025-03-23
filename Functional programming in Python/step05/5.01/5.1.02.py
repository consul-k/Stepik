res = {}

def factorial(n):
    global res
    number = 1
    if n not in res:
        for i in range(1,n+1):
            number *= i
        res[n] = number
        return res[n]
    else:
        return f'Get from cache value factorial({n})\n{res[n]}'
