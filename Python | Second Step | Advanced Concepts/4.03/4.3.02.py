numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

even_numbers = {i for i in numbers if i%2==0}
numbers = {i for i in numbers if i%5!=0}

print(sorted(list(numbers)))
print(sorted(list(even_numbers)))
