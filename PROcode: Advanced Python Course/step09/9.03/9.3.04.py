orchard = {
    "apple", "pear", "peach", "plum", "cherry",
    "banana", "orange", "lime", "lemon", "grapefruit",
    "mango", "papaya", "pineapple", "kiwi", "strawberry",
    "blueberry", "raspberry", "grape", "melon", "watermelon"
}

N = int(input())
for _ in range(N):
    command = input().strip().split()
    
    if command[0] == "add":
        orchard.add(command[1])
    elif command[0] == "remove":
        orchard.remove(command[1])
    elif command[0] == "discard":
        orchard.discard(command[1])
    elif command[0] == "pop":
        if orchard:
            orchard.pop()
    elif command[0] == "clear":
        orchard.clear()

if orchard:
    print(" ".join(sorted(orchard)))
else:
    print("Фруктовый сад пуст")
