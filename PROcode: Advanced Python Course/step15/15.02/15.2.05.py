input_str = input().strip()

potions = [potion.strip() for potion in input_str.split(',')]

unique_potions = sorted(set(potions))

total_count = len(potions)

unique_count = len(unique_potions)

max_count = 0
most_common_potion = None

count_dict = {}
for potion in potions:
    if potion not in count_dict:
        count_dict[potion] = 0
    count_dict[potion] += 1

for potion in unique_potions:
    if count_dict[potion] > max_count:
        max_count = count_dict[potion]
        most_common_potion = potion

print(f"Уникальные зелья: {unique_potions}")
print(f"Всего зелий: {total_count}")
print(f"Количество уникальных зелий: {unique_count}")
print(f"Самое частое зелье: {most_common_potion} ({max_count} раз(а))")
