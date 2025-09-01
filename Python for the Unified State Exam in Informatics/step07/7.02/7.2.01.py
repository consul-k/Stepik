n = int(input())
data = []
for i in range(n):
    new = int(input())  # считывание очередного значения
    data += [new]       # добавление значения в список

mihail_sum = 0
zhanna_sum = 0

for price in data:
    if price % 2 == 0:
        mihail_sum += price
    else:
        zhanna_sum += price

print(mihail_sum)
print(zhanna_sum)
