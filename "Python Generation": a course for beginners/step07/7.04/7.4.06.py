res = []
n = int(input())
while n > 0 and n <= 5:
    if n == 5:
        res.append(n)
    n = int(input())
print(len(res))
