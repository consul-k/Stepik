import sys
lst = [i.rstrip() for i in sys.stdin.readlines()]

res = {}
for i in lst:
    sin, sinner = i.split()
    res[sin] = res.get(sin, []) + [sinner]

print(res)
