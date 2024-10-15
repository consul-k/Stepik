def find_first_same_sign_pair(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] * numbers[i + 1] > 0:
            print(numbers[i], numbers[i + 1])
            break

numbers = list(map(int, input().split()))
find_first_same_sign_pair(numbers)
