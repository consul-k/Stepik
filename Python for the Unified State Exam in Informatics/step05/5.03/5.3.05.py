count = 0

while True:
    s = input()
    if s == "СТОП":
        break
    num = int(s)
    if num < 0 and num % 2 != 0:
        count += 1

print(count)
