def check(l, n):
    if l[0] < n < l[1]:
        return True
    return False

l = list(map(int, input().split()))
n = int(input())
print(check(l, n))
