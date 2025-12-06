n = int(input())

enemies = []

for _ in range(n):
    name = input().strip()
    damage = int(input())
    armor = int(input())
    
    enemies.append({
        'name': name,
        'damage': damage,
        'armor': armor,
        'threat': damage + armor
    })

strongest_enemy = max(enemies, key=lambda x: x['threat'])

my_damage = 60
final_damage = max(0, my_damage - strongest_enemy['armor'])

battle_result = "Победа" if final_damage > 0 else "Поражение"

print(f"Самый опасный враг: {strongest_enemy['name']}")
print(f"Уровень угрозы: {strongest_enemy['threat']}")
print(f"Итоговый урон по врагу: {final_damage}")
print(f"Исход боя: {battle_result}")
