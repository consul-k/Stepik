dogs_input = input().split()
cats_input = input().split()
parrots_input = input().split()

dogs_set = set(map(int, dogs_input)) if dogs_input[0] != '' else set()
cats_set = set(map(int, cats_input)) if cats_input[0] != '' else set()
parrots_set = set(map(int, parrots_input)) if parrots_input[0] != '' else set()

def format_set(s):
    if not s:
        return "set()"
    return "{" + ", ".join(map(str, sorted(s))) + "}"

print(f"Сторонники партии собак: {format_set(dogs_set)}")
print(f"Сторонники партии кошек: {format_set(cats_set)}")
print(f"Сторонники партии попугаев: {format_set(parrots_set)}")

dogs_count = len(dogs_set)
cats_count = len(cats_set)
parrots_count = len(parrots_set)

print(f"Общее количество сторонников партии собак: {dogs_count}")
print(f"Общее количество сторонников партии кошек: {cats_count}")
print(f"Общее количество сторонников партии попугаев: {parrots_count}")

dogs_cats_intersection = dogs_set & cats_set
dogs_parrots_intersection = dogs_set & parrots_set
cats_parrots_intersection = cats_set & parrots_set

print(f"Общие сторонники между собаками и кошками: {format_set(dogs_cats_intersection)}")
print(f"Общие сторонники между собаками и попугаями: {format_set(dogs_parrots_intersection)}")
print(f"Общие сторонники между кошками и попугаями: {format_set(cats_parrots_intersection)}")

counts = {
    "собак": dogs_count,
    "кошек": cats_count,
    "попугаев": parrots_count
}

max_count = max(counts.values())
winners = [party for party, count in counts.items() if count == max_count]

if len(winners) == 3:
    print("Ой-ой! Похоже, выборы были отменены! Все партии набрали одинаковое количество сторонников! 😹")
else:
    winner_party = winners[0]
    if winner_party == "собак":
        print("Победила партия собак с наибольшим количеством сторонников! 🐶🎉")
    elif winner_party == "кошек":
        print("Победила партия кошек с наибольшим количеством сторонников! 🐱🎉")
    else:
        print("Победила партия попугаев с наибольшим количеством сторонников! 🦜🎉")
