import math

S = float(input())
D = float(input())
N = int(input())

count = 0

while count < N:
    sin_value = math.sin(S)
    if sin_value >= 0.5:
        print(f"{S:.3f} {sin_value:.3f}")
        count += 1
    S += D
