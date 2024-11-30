input_string = input()

surnames = input_string.split()

sorted_surnames = sorted(surnames)

output_string = ",".join(sorted_surnames)

print(output_string)
