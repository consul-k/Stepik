def can_break_chocolate(N, M, K):
    if K < N * M and (K % N == 0 or K % M == 0):
        return "YES"
    else:
        return "NO"

N = int(input())
M = int(input())
K = int(input())

print(can_break_chocolate(N, M, K))
