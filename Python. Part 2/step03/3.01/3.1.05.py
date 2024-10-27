res = []
i = int(input())

while i >= 0:
    res.append(i)
    i = int(input())
print(f'Максимальное введенное число: {max(res)}')
