initial_data = input()
additions = input()
removals = input()

initial_set = set(map(str.strip, initial_data.split(',')))
add_set = set(map(str.strip, additions.split(',')))
remove_set = set(map(str.strip, removals.split(',')))

result_set = (initial_set | add_set) - remove_set

sorted_result = sorted(result_set)
formatted_output = "{" + ", ".join(sorted_result) + "}"

print(formatted_output)
