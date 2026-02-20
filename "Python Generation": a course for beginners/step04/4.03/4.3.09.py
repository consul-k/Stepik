a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

left = max(a1, a2)
right = min(b1, b2)

if left < right:
    print(left, right)
elif left == right:
    print(left)
else:
    print("пустое множество")
