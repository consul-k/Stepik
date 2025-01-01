input_string = input()

names = input_string.split()

unique_names = list(set(names))

filtered_names = [name for name in unique_names if not name.startswith('Р')]

if "Алон" not in filtered_names:
    filtered_names.append("Алон")
if "Эйли" not in filtered_names:
    filtered_names.append("Эйли")

sorted_names = sorted(filtered_names)

print(sorted_names)
