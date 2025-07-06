input1 = input()
input2 = input()

tuple1 = tuple(input1.split())
tuple2 = tuple(input2.split())

combined = tuple1 + tuple2

unique_chars = ()
for item in combined:
    if item not in unique_chars:
        unique_chars += (item,)

if len(unique_chars) % 2 == 0:
    result = tuple(sorted(unique_chars))
else:
    result = unique_chars[::-1]

print(result)
