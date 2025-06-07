a = input().split(', ')
for word in a:
    if word == 'danger':
        print('След обнаружен! Мы нашли сигнал тревоги: danger')
        break
else:
    print('Сигнал тревоги не найден. Мы продолжаем поиски.')
