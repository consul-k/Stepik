N = int(input())

catalog = {}

for _ in range(N):
    entry = input()
    manufacturer, model = entry.split(' ', 1)
    catalog[model] = manufacturer


search_model = input()

if search_model in catalog:
    print(catalog[search_model])
else:
    print("В нашем каталоге нет такого автомобиля.")
