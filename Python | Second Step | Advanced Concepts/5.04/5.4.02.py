dict1 = {"A": {"x": 1, "y": 2}, "B": {"z": 3}}
dict2 = {"A": {"y": 5, "w": 8}, "C": {"k": 7}}

result = dict1.copy()

for key, subdict in dict2.items():
    if key in result and isinstance(result[key], dict) and isinstance(subdict, dict):
        result[key] = {**result[key], **subdict}
    else:
        result[key] = subdict

print(result)
