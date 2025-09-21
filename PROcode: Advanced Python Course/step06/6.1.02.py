a = int(input())
b = int(input())
c = int(input())

numbers_tuple = (a, b, c)

numbers_list = list(numbers_tuple)
numbers_list.sort()

sorted_tuple = tuple(numbers_list)

middle_value = sorted_tuple[1]
middle_index = sorted_tuple.index(middle_value)

print(middle_value)
