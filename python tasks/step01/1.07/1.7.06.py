def max_divisor(N):
    for i in range(N-1, 0, -1):
        if N % i == 0:
            return i

N = int(input())
print(max_divisor(N))
