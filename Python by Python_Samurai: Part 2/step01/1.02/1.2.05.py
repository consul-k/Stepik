a = input().split()
for word in a:
    if len(word) <= 4:
        print('НЕТ')
        break
else:
    print('ДА')
