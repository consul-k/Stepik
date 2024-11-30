n = int(input())

catalog = {}

# Заполняем каталог
for _ in range(n):
    entry = input()
    manufacturer, model = entry.split(' ', 1)
    if manufacturer not in catalog:
        catalog[manufacturer] = []
    catalog[manufacturer].append(model)

search_manufacturer = input()

if search_manufacturer in catalog:
    print(" ".join(sorted(catalog[search_manufacturer])))
else:
    print("В нашем каталоге нет автомобилей этого производителя.")
