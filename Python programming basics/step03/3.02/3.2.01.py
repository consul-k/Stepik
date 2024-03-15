n = int(input(" "))
a = n
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f'Факториал числа {a} равен {factorial}')
