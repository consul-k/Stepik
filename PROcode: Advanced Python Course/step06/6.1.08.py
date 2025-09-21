input_str = input()

symbols = tuple(input_str.split())

if len(symbols) < 3:
    print("Ошибка! Недостаточно символов!")
elif 3 <= len(symbols) <= 6:
    result = symbols[-3:]
    print(result)
else:  # len(symbols) > 6
    result = symbols[:3] + symbols[-3:]
    print(result)
