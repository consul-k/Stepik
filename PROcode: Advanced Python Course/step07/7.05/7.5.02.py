import sys

input_data = sys.stdin.read().strip().split('\n')

anime_list = []
for line in input_data:
    parts = line.split(', ')
    title = parts[0].split(': ')[1]
    episodes = parts[1].split(': ')[1]
    genre = parts[2].split(': ')[1]
    watched = parts[3].split(': ')[1] == 'True'
    
    anime_list.append({
        'title': title,
        'episodes': episodes,
        'genre': genre,
        'watched': watched
    })

print("Просмотренные аниме:")
for anime in anime_list:
    if anime['watched']:
        print(anime['title'])

print()

print("Аниме, которые хотите посмотреть:")
for anime in anime_list:
    if not anime['watched']:
        print(anime['title'])

print()

print(f"Аниме в жанре {target_genre}:")
for anime in anime_list:
    if anime['genre'] == target_genre:
        print(anime['title'])
