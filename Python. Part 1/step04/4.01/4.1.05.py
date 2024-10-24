n = int(input())
if n < 0:
    print('Холодная погода.')
elif n <= 15:
    print('Прохладная погода.')
elif n <= 30:
    print('Теплая погода.')
elif n > 30:
    print('Жаркая погода.')
