number = int(input())

sum_digits = 0
count_digits = 0
product_digits = 1
number_copy = number

first_digit = int(str(number)[0])

last_digit = number % 10

while number > 0:
    digit = number % 10
    sum_digits += digit
    count_digits += 1
    product_digits *= digit
    number //= 10

average_digits = sum_digits / count_digits

sum_first_last_digits = first_digit + last_digit

print(sum_digits)
print(count_digits)
print(product_digits)
print(average_digits)
print(first_digit)
print(sum_first_last_digits)
