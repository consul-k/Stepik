def translate(num, base=2):
    digits = "0123456789"
    new_num = ""
    while num > 0:
        digit = digits[num % base]
        new_num = digit + new_num
        num //= base
    return new_num
