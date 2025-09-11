start = int(input())
position = start * 2

if start % 2 == 1:
    position *= 3
else:
    position //= 3

position //= 2

position += 5


print(f"Конечная позиция Счетчика: {position}")
