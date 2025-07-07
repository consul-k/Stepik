pets = eval(input())

owners_dict = {}

for dog_name, first_name, last_name, age in pets:
    owner_key = (first_name, last_name, age)
    if owner_key not in owners_dict:
        owners_dict[owner_key] = []
    owners_dict[owner_key].append(dog_name)

print(owners_dict)
