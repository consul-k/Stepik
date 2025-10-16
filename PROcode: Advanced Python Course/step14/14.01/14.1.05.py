import re

with open("fragments.txt", "r", encoding="utf-8") as f:
    text = f.read()

numbers = re.findall(r'-?\d+', text)

print(" ".join(numbers))
