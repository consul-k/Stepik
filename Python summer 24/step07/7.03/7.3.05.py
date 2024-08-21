import re

def convert_to_pythom_case(text):
    return re.sub('([A-Z][a-z]*)', r'\1_', text).lower().rstrip('_')

print(convert_to_pythom_case(input()))
