inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 7,
    "grapes": 3,
    "melon": 2
}

inventory["apple"] += 5
inventory["banana"] += 2
print("После добавления элементов:", inventory)

inventory.pop("orange", None)
if "grapes" in inventory:
    inventory["grapes"] -= 1
    if inventory["grapes"] <= 0:
        inventory.pop("grapes")
print("После удаления элементов:", inventory)

inventory["watermelon"] = 4
print("После обновления значений:", inventory)

if "melon" in inventory:
    print("Количество арбузов (melon):", inventory["melon"])
print("После проверки наличия элемента:", inventory)


removed_item = inventory.popitem()
print("Удаленный элемент:", removed_item)
print("После использования popitem():", inventory)

inventory.clear()
print("После очистки инвентаря:", inventory)
