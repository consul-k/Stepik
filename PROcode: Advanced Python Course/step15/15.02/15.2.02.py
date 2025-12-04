inventory_input = input()

items = [item.strip() for item in inventory_input.split(',')]

print(items)

print(f"Всего предметов: {len(items)}")

shortest_item = min(items, key=len)
print(f"Самый короткий предмет: {shortest_item}")

longest_item = max(items, key=len)
print(f"Самый длинный предмет: {longest_item}")
