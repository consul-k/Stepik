n = int(input())
fan_tracks = {}

for _ in range(n):
    line = input()
    first_space = line.find(' ')
    name = line[:first_space]
    track = line[first_space + 1:]
    fan_tracks[name] = track

print(fan_tracks)
