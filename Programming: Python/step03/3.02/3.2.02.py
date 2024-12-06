def check_unique_digits(number):
    num_str = str(number)

    if len(num_str) != 3:
        return "Число не является трёхзначным"

    if len(set(num_str)) == 3:
        return "Цифры различны"
    else:
        return "Цифры не различны"

number = int(input())
result = check_unique_digits(number)
print(result)
