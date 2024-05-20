n = int(input())
def donuts(n):
    if n <= 9:
        return f'Всего пончиков: {n}'
    else:
        return 'Всего пончиков: много'

print(donuts(n))
