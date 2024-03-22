number = int(input())

power = 0
value = 1

while value < number:
    value *= 2
    power += 1

if value == number:
    print("YES")
else:
    print("NO")
