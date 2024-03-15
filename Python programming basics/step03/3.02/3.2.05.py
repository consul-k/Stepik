n = int(input(""))

def fbnci(n):
    Fibonacci = [0]
    f0 = 0; f1 = 1
    for i in range(n):
        f0, f1 = f1, f0 + f1
        Fibonacci.append(f0)
    return(Fibonacci)

res = fbnci(n)
res.pop()
print(*res)
