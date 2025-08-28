def function(x):
    if len(x) == 1: return 3
    elif len(x) == 2: return 2
    return 0
    
a,b,c = str(input()),str(input()),str(input())
f = set(a + b + c)
print(function(f))
