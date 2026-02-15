n = int(input())

fib1 = 1
fib2 = 1

if n == 1:
    print(fib1)
elif n == 2:
    print(fib1, fib2)
else:
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib_next = fib1 + fib2
        print(fib_next, end=' ')
        fib1, fib2 = fib2, fib_next
