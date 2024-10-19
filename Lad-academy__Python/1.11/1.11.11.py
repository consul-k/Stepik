def s(l):
    return sorted(set(l))

a = list(map(int, input().split()))
print(*s(a))
