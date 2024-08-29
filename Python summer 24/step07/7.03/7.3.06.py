def is_palindrome(n:int)->bool:
    return str(n) == str(n)[::-1]

def is_prime(n:int)->bool:
    if n in (0, 1):
        return False
    if n%2 == 0:
        return False
    for i in range(3, round(n**(1/2)+1), 2):
        if n%i == 0:
            return False
    return True

def is_even(n:int)->bool:
    return n%2 == 0


a, b, c = map(int, input().split(':'))
if is_palindrome(a) and is_prime(b) and is_even(c):
    print(True)
else:
    print(False)
