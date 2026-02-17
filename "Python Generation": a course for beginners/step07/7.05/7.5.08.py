pos_alexandra = -1
pos_levon = -1
current_pos = 0

while True:
    try:
        name = input()
        if name == "Александра":
            pos_alexandra = current_pos
        elif name == "Левон":
            pos_levon = current_pos
        current_pos += 1
    except EOFError:
        break

count_between = pos_levon - pos_alexandra - 1
print(count_between)
