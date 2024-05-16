n = ''
l = 0

while True:
    n = input()
    if n != 'The End':
        l += int(n)
    else:
        break
print(l)
