ingredient1 = ("Фениксова перо", 5, "Очень редкий", "Воскрешение")
ingredient2 = ("Лунный камень", 3, "Редкий", "Усиление магии")
ingredient3 = ("Черный песок", 2, "Обычный", "Защита от огня")

ingredients = [ingredient1, ingredient2, ingredient3]

index = int(input())

if 0 <= index < len(ingredients):
    name, power, rarity, effect = ingredients[index]
    print(f"Название: {name}")
    print(f"Сила: {power}")
    print(f"Редкость: {rarity}")
    print(f"Эффект: {effect}")
else:
    print("Ошибка: введите число 0, 1 или 2.")
