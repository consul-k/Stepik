def characterize_string(s):
    if len(s) % 2 == 0:
        parity = "четная"
    else:
        parity = "нечетная"

    if len(s) < 6:
        length = "короткая"
    else:
        length = "большая"

    print(f"{parity} {length}")

input_string = input()
characterize_string(input_string)
