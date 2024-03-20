n = int(input())
res = ''
res += str(n%10)
res += str(n//100%10)
res += str(n//10%10)
res += str(n//1000)

print(int(res))
