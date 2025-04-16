def gen_arithmetic_progression(first, difference):
    current = first
    while True:
        yield current
        current += difference
