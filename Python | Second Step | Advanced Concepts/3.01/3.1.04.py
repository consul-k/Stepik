data = ("apple", "banana", "cherry", "apple", "date", "banana", "cherry", "fig")

unique_list = list(set(data))

unique_list.sort()

result = tuple(unique_list)

print(result)
