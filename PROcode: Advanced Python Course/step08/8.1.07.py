import json

dictionary_input = input()

encrypted_input = input()

decoder = json.loads(dictionary_input)

codes = encrypted_input.split()

result = ""

for code in codes:
    if code in decoder:
        result += decoder[code]
    else:
        result += "?"

print(result)
