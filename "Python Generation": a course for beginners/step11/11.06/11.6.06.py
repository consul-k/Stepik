n = int(input())

songs = []
for _ in range(n):
    song = input()
    songs.append(song)

songs.sort()

for song in songs:
    print(song)
