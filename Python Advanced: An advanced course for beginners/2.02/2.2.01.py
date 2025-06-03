def detect_type(value):
    if value == 'True' or value == 'False':
        return bool
    try:
        int(value)
        return int
    except ValueError:
        try:
            float(value)
            return float
        except ValueError:
            return str

values = [input() for _ in range(4)]

types = [detect_type(val) for val in values]

print(f"Тип первого значения: <class '{types[0].__name__}'>")
print(f"Тип второго значения: <class '{types[1].__name__}'>")
print(f"Тип третьего значения: <class '{types[2].__name__}'>")
print(f"Тип четвертого значения: <class '{types[3].__name__}'>")
