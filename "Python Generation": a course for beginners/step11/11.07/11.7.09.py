a = list(map(int, input().split()))
res = [i**2 for i in a if i%2==0 and i**2%10!=4]
print(*res)
