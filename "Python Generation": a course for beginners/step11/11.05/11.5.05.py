a = list(map(int, input().split('.')))
for n in a:
    if n < 0 or n > 255:
        print('НЕТ')
        break
else:
    print('ДА')
