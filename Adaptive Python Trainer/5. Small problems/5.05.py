def int_to_roman(n: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return (
        thousands[n // 1000] +
        hundreds[(n % 1000) // 100] +
        tens[(n % 100) // 10] +
        ones[n % 10]
    )


n = int(input().strip())
print(int_to_roman(n))
