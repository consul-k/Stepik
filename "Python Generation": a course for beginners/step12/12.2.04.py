import re

def is_valid_phone_number(phone_number):
    pattern = r'^(7-)?\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return "YES"
    else:
        return "NO"

phone_number = input()

result = is_valid_phone_number(phone_number)

print(result)
