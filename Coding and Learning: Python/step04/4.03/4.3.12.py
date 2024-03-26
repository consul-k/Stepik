N = int(input())

numbers = [x for x in range(N+1)]
primes = []

for i in range(2, N+1):
    if numbers[i] != 0:
        primes.append(numbers[i])
        for j in range(i*2, N+1, i):
            numbers[j] = 0

print(primes)
