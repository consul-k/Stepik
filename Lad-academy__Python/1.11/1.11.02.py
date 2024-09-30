def arithmetic(a,b,s):
    if s == '+':
        return a+b
    elif s == '-':
        return a-b
    elif s == '*':
        return a*b
    elif s == '/':
        if b == 0:
            return 'Invalid operation'
        else:
            return a/b
    else:
        return 'Invalid operation'
        
data = input().split()
a = int(data[0])
b = int(data[1])
s = data[2]
print(arithmetic(a,b,s))
