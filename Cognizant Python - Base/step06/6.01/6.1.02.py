def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

user_input = input()

result = convert_to_float(user_input)

print(result)
