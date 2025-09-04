n = int(input())
has_max_score = False 

for _ in range(n):
    score = int(input())
    if score == 100:
        has_max_score = True
        break

print(has_max_score)
