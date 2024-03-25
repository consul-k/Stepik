numbers = []
total = 0
count = 0

num = int(input())

while num != 0:
    numbers.append(num)
    total += num
    count += 1
    num = int(input())

if count > 0:
    average = total / count
    print(average)
else:
    print("Вы не ввели ни одного числа!")
