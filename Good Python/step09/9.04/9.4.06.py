def s(a,b,c):
    if a+b<=c or a+c<=b or c+b<=a:
        return -1
    else:
        p=(a+b+c)/2
        return(p*(p-a)*(p-b)*(p-c))**0.5

a = float(input())
b = float(input())
c = float(input())

print(round(s(a,b,c),3))
