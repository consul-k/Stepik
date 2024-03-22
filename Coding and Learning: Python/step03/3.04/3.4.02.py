from string import ascii_uppercase as up

for i in map(int, input().split()):
    if 0 < i < 27:
        print(up[i - 1])
    else:
        print("Неверное число")
