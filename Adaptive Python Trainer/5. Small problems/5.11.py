import sys

a = list(map(int, sys.stdin.read().split()))
n = len(a)

if n <= 1:
    print("Jolly")
else:
    diffs = set()
    for i in range(n - 1):
        d = abs(a[i + 1] - a[i])
        if d == 0 or d >= n:  # допустимы только 1..n-1
            print("Not jolly")
            break
        diffs.add(d)
    else:
        print("Jolly" if len(diffs) == n - 1 else "Not jolly")
