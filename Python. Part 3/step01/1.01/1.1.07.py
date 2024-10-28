common_dict = {key: d1[key] for key in d1 if key in d2 and d1[key] == d2[key]}

print(common_dict)
