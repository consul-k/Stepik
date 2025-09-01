numbers = []
squares = []
cubes = []

for i in range(1, 11):
    numbers.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)

# Вывод списков
print(' '.join(str(num) for num in numbers))
print(' '.join(str(num) for num in squares))
print(' '.join(str(num) for num in cubes))
