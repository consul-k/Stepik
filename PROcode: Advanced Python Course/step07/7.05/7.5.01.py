anime_characters = {
    "Naruto": {"age": 17, "favorite_anime": "Naruto Shippuden"},
    "Luffy": {"age": 19, "favorite_anime": "One Piece"}
}

name = input()
age = int(input())
favorite_anime = input()
anime_characters[name] = {"age":age, "favorite_anime":favorite_anime}

print("Информация о всех персонажах:\n")
for character_name, info in anime_characters.items():
    print(f'Имя: {character_name}')
    print(f'Возраст: {info["age"]}')
    print(f'Любимое аниме: {info["favorite_anime"]}')
    print()
