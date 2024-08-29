def count_local_maxima():
    sequence = []

    while True:
        num = int(input())
        if num == 0:
            break
        sequence.append(num)

    local_maxima_count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1]:
            local_maxima_count += 1

    return local_maxima_count

print(count_local_maxima())
