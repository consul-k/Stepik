import random

a = input()

r = random.randint(0, 36)

if a == "красное":
    if r >= 0 and r <= 11:
        print("ставка сыграла")
    else:
        print("ставка не сыграла")
elif a == "черное":
    if r >= 12 and r <= 23:
        print("ставка сыграла")
    else:
        print("ставка не сыграла")
elif a == "зеленое":
    if r >= 24 and r <= 36:
        print("ставка сыграла")
    else:
        print("ставка не сыграла")
