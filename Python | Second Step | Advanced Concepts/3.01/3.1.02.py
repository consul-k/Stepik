numbers = input().split()

numbers = [int(num) for num in numbers]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
unique_tuple = tuple(unique)

counts = tuple((num, numbers.count(num)) for num in unique_tuple)

print("Кортеж уникальных элементов:", unique_tuple)
print("Количество встречающихся элементов:", counts)
