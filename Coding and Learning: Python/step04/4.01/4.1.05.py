numbers = []
current = int(input())

while current != 0:
    numbers.append(current)
    current = int(input())

print(min(numbers))
