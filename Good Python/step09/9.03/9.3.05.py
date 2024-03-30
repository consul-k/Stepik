def s(a,b,c):
    return 2*(a*b + a*c + b*c)

a, b, c = [int(i) for i in input().split()] 

print(s(a, b, c))
