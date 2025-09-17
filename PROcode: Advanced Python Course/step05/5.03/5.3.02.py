import re

input_str = input()
tuples = [tuple(map(int, match)) for match in re.findall(r'\((\d+),\s*(\d+)\)', input_str)]

min_tuple = min(tuples, key=lambda x: x[0])
max_tuple = max(tuples, key=lambda x: x[0])

print("Кортеж с минимальным первым элементом:", min_tuple)
print("Кортеж с максимальным первым элементом:", max_tuple)
