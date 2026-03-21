def math_round_to_int(num):
    integer_part = int(num)
    fractional_part = num - integer_part
    
    if fractional_part < 0.5:
        return integer_part
    else:
        return integer_part + 1

num = float(input())

print(math_round_to_int(num))
