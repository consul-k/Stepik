negative = []
positive = []
zero = []

for _ in range(int(input())):
    i = int(input())
    if i < 0:
        negative.append(i)
    elif i == 0:
        zero.append(i)
    else:
        positive.append(i)
for i in negative:
    print(i)
for i in zero:
    print(i)
for i in positive:
    print(i)
