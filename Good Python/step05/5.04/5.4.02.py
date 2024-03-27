s, i = int(input()), 0
while True:
    n = int(input())
    s -= n
    if s <= 0:
        i += (s == 0)
        break
    i+=1
print(i)
