N = int(input())

car_set = set()

for _ in range(N):
    command = input().split()
    if command[0] == "add":
        car_set.add(command[1])
    elif command[0] == "remove":
        car_set.remove(command[1])
    elif command[0] == "discard":
        car_set.discard(command[1])
    elif command[0] == "pop":
        if car_set:
            car_set.pop()
    elif command[0] == "clear":
        car_set.clear()

if not car_set:
    print("Множество пустое")
else:
    print(" ".join(car_set))
