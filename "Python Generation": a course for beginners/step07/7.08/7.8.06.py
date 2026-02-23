name = input()
while len(name) < 10:
    if len(name) % 4 == 0:
        name = name + 'x'
    elif len(name) % 5 == 0:
        name = name + 'y'
    else:
        name = 'z' + name
name = '@' + name
print(name)
