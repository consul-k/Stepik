monsters = {
    "Шшшшшш": ("Вампир", 10),
    "Аууууу": ("Вурдалак", 13),
    "Рррррр": ("Оборотень", 8),
    "Уууууу": ("Призрак", 14),
    "Гррррр": ("Демон", 21)
}

sounds = input().split()

monster_name = None
hp = 0

for sound in sounds:
    if sound in monsters:
        monster_name, hp = monsters[sound]
        break

if monster_name:
    print(f"Монстр пойман! Это {monster_name}! Битва начинается!")
    turn = 0  # 0 = Дон, 1 = Сим

    while hp > 0:
        if turn == 0:
            attacker = "Дона"
        else:
            attacker = "Сима"

        hp -= 2
        if hp < 0:
            hp = 0
        print(f"Ход {attacker}: {monster_name} получает 2 урона! У {monster_name} осталось {hp} жизней.")

        if hp == 0:
            print(f"{monster_name} убит!")
            break

        turn = 1 - turn
