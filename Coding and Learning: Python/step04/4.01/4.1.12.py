numbers = []
position = 1
num = int(input())

while num != 0:
    numbers.append(num)
    num = int(input())

maximum = max(numbers)
print(numbers.index(maximum) + 1)
