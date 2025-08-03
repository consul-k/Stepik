n = int(input())

names = []
for _ in range(n):
    name = input()
    names.append(name)

scores = []
for _ in range(n):
    score = int(input())
    scores.append(score)

result = list(zip(names, scores))

print(result)
