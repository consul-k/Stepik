numbers = input().split()

numbers = [int(num) for num in numbers]

positive_sum = sum(num for num in numbers if num > 0)

negative_sum = sum(num for num in numbers if num < 0) * 2

total_power = positive_sum + negative_sum

if total_power < 10:
    total_power *= 2

print(f"Сила камней: {total_power}")
