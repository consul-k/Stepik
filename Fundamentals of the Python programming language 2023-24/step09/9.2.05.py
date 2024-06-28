n = int(input())

prev_set = set(map(int, input().split()))

for _ in range(n - 1):
    current_set = set(map(int, input().split()))

    if current_set.issubset(prev_set):
        print("YES")
    else:
        print("NO")

    prev_set = current_set
