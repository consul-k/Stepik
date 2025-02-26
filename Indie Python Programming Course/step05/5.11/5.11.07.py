a, b = map(int, input().split())
s = [i**2 for i in range(a,b+1)] if a<=b else [i**3 for i in range(a,b-1,-1)]
print(s)
