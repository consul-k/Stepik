required_input = input().split(',')
required_skills = {skill.strip() for skill in required_input}

n = int(input())

matching_players = []

for _ in range(n):
    line = input()
    parts = line.split(':')
    name = parts[0].strip()
    
    player_skills_str = parts[1]
    player_skills = {skill.strip() for skill in player_skills_str.split(',')}
    
    if player_skills.issuperset(required_skills):
        matching_players.append(name)

if matching_players:
    print(f"Игроки с полным набором навыков: {', '.join(matching_players)}")
else:
    print("Нет игроков с полным набором навыков")
