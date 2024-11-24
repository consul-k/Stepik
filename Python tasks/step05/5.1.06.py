def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_composite(n):
    """Функция для проверки, является ли число составным."""
    return n > 1 and not is_prime(n)

# Ввод числа
number = input()

# Проверяем первую и последнюю цифры
first_digit = int(number[0])
last_digit = int(number[-1])

# Проверяем остальные цифры
middle_digits = number[1:-1]

if is_prime(first_digit) and is_prime(last_digit):
    if all(is_composite(int(digit)) for digit in middle_digits):
        print("True")
    else:
        print("False")
else:
    print("False")
