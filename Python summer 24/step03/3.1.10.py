sequence = []

while True:
    num = int(input())
    if num == 0:
        break
    sequence.append(num)

if sequence:
    max_value = max(sequence)

    count_max = sequence.count(max_value)

    print(count_max)
else:
    print(0)
