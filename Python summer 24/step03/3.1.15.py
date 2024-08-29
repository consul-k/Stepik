def analyze_number(number):
    odd_count = 0
    even_product = 1
    has_even = False

    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            even_product *= digit
            has_even = True
        else:
            odd_count += 1

    if not has_even:
        even_product = 0

    print(odd_count, even_product)

number = int(input())
analyze_number(number)
