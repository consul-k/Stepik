n, m = int(input()), int(input())

def rectangle(n,m):
    for _ in range(n):
        print('*'*m)

rectangle(n,m)
print()

rectangle(3,4)
print()

rectangle(m,n)
print()

rectangle(5,5)
print()

print(("*" * n + "\n") * m)
