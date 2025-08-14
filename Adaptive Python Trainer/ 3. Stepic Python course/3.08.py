n = int(input())
res = [[0] * n for j in range(n)]
ai, aj = 0, 0
di, dj = 0, 1
for k in range(1, n ** 2 + 1):
    res[ai][aj] = k
    if dj != 0 and (aj + dj == n or aj + dj < 0 or res[ai][aj + dj] != 0):
        di, dj = dj, di
    if di != 0 and (ai + di == n or ai + di < 0 or res[ai + di][aj] != 0):
        di, dj = dj, -di
    ai += di
    aj += dj
for i in res:
    print(*i)
