def swap_min_max(sequence):
    if not sequence:
        return sequence

    min_index = 0
    max_index = 0

    for i in range(len(sequence)):
        if sequence[i] < sequence[min_index]:
            min_index = i
        if sequence[i] > sequence[max_index]:
            max_index = i

    sequence[min_index], sequence[max_index] = sequence[max_index], sequence[min_index]

    return sequence

def main():
    sequence = []

    while True:
        number = int(input())
        if number == 0:
            break
        sequence.append(number)

    result = swap_min_max(sequence)
    for num in result:
        print(num)

if __name__ == "__main__":
    main()
