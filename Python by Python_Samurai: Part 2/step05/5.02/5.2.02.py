lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# продолжите решение здесь
def is_even(num):
    return num % 2 == 0

for num in lst:
    if is_even(num):
        print(num)
