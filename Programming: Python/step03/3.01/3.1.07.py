x = int(input())
if (x // 10) % 2 == 0 and (x % 10)%2 == 0:
    x += 2
else:
    x -= 2
print(x)
