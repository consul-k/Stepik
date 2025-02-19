n = int(input())

st = 0
while n%2 == 0:
    st += 1
    n //= 2
if n == 1:
    print(st)
else:
    print('НЕТ')
