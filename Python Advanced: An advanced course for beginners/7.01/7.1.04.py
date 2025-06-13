n = int(input())

res = dict()

while True:
    try:
        line = input()
        if not line:
            break
        island, gold = line.split(":")
        res[island.strip()] = int(gold.strip())
    except:
        break

for island in res:
    res[island] = res[island] // n

for island, gold_per_person in res.items():
    print(f"{island}: {gold_per_person}")
