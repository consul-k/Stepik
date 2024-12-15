def solve_equation(a, b):
    if a == 0:
        if b == 0:
            return "INF"
        else:
            return "NO"
    else:
        if -b % a == 0:
            return str(-b // a)
        else:
            return "NO"

a = int(input())
b = int(input())
print(solve_equation(a, b))
