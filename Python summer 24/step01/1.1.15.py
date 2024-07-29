A = int(input())
B = int(input())
N = int(input())

total = (A * 100 + B) * N

r = total // 100
k = total % 100

print(r, k)
