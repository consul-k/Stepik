numbers = [int(i) for i in input().split()]
num_set = set()
for n in numbers:
    if n in num_set:
        print('YES')
    else:
        print('NO')
    num_set.add(n)
