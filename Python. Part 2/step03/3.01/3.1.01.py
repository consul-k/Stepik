res = 0
numbers = int(input())

while numbers != 0:
    res += numbers
    numbers = int(input())
print(f'Сумма всех чисел: {res}')
