n = int(input())

names = []
symbols = []
numbers = []

for _ in range(n):
    names.append(input())
    symbols.append(input())
    numbers.append(int(input()))

search_symbol = input()

print("Список элементов:")
for i in range(n):
    print(f"{i+1}. {names[i]} ({symbols[i]}) - атомный номер: {numbers[i]}")

print()

found = False
for i in range(n):
    if symbols[i] == search_symbol:
        print(f"Атомный номер элемента {search_symbol}: {numbers[i]}")
        found = True
        break

if not found:
    print(f"Элемент с символом {search_symbol} не найден.")
