p = int(input())
melon = 0
wmelon = 0
for i in range(0, p):
    frukt = input()
    if frukt == "дыня":
        melon += 1
    elif frukt == "арбуз":
        wmelon += 1
if melon > wmelon:
    print("Дыни популярнее")
elif wmelon > melon:
    print("Арбузы популярнее")
elif melon == wmelon: 
    print("Арбузы и дыни одинаково популярны")
