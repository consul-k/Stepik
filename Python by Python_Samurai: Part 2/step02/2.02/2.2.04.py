users = {
    "Николя": ["кружка", "стакан", "рюмка"],
    "Брагин Вовчик": ["лифчик", "косметика", "тостер", "плюшевый мишка"],
    "Хайзенберг": ["мерная колба", "спирт", "огурчик"],
    "Ирина Михайловна": ["тостер", "микроволновка", "несущая стена"],
    "Кратос": ["топор", "доспехи", "умная колонка", "тостер"]
}

# продолжите решение здесь
a = input()
names = []
for key, value in users.items():
    if a in value:
        names.append(key)
if len(names) == 0:
    print(f"{a} отсутствует в корзинах пользователей")
else:
    print(f"{a} в корзине у {', '.join(names)}")
