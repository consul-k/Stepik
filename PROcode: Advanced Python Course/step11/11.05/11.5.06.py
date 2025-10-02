n = int(input())
artefacts = [tuple(map(str.strip, input().split(','))) for _ in range(n)]

artefacts = list(map(lambda x: (x[0], int(x[1]), float(x[2])), artefacts))

filtered = list(filter(lambda x: x[1] >= 2000, artefacts))

updated = list(map(lambda x: (x[0], x[1], x[2] * 1.25), filtered))

sorted_artefacts = sorted(updated, key=lambda x: x[2])

print("Артефакты после обработки:")
print(sorted_artefacts)
