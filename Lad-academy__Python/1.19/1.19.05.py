n = input().split()

def isort(n):
    num = 0
    for i in range(len(n)):
        num += int(n[i])
    return num

print(*sorted(n, key=isort))
