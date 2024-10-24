n = int(input())
if  n <= 24 and n >= 0:
    if 9 <= n <= 18:
        print("Магазин открыт.")
    elif n > 18 or n < 9:
        print("Магазин закрыт.")
else:
    print("Время указано неверно.")
