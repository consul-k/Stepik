seats = list(range(1, 11))
bought = 0

while bought < 5:
    seat = int(input())
    if seat < 1 or seat > 10:
        continue
    if seats[seat - 1] == "x":
        continue

    seats[seat - 1] = "x"
    bought += 1

print(seats)
