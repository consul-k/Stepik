a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Все равны")
elif a == b or b == c or a == c:
    print("Два равны")
else:
    print("Все различны")
