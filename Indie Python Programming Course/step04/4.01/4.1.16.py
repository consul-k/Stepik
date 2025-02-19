n=int(input())
while int(str(n)[0])!=1 and n<=1000000000:
    n*=int(str(n)[0])
print(n)
