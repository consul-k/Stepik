athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def by_name(athlet):
    return athlet[0]

def by_age(athlet):
    return athlet[1]

def by_height(athlet):
    return athlet[2]

def by_weight(athlet):
    return athlet[3]

commands = {1: by_name, 2: by_age, 3: by_height, 4: by_weight}
command = int(input())

for i in sorted(athletes, key = commands[command]):
    print(*i)
