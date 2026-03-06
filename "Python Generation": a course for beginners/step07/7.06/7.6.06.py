n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)
