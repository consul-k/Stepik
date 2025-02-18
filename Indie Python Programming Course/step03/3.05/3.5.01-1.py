age = int(input())
member = bool(int(input()))

if age > 18 and member:
    print("Цена билета 75")
elif age > 18:
    print("Цена билета 100")
elif member:
    print("Цена билета 25")
else:
    print("Цена билета 50")
