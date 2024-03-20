n = int(input())
res = ''

res += str(n//10000)
res += str(n//1000%10)

res += str(n//10%10)
res += str(n%10) 

print(int(res))
