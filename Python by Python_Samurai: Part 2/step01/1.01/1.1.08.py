nif, naf = map(int, input().split())
years = 0

while nif <= naf:
    nif *= 3
    naf *= 2
    years += 1

print(years)
