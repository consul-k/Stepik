def sum_even_dig(n):
    even_sum = sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)
    return even_sum
