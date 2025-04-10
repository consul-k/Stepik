def uppercase(func):
    def inner(n, i, rate):
        res = func(n, i, rate)
        return res.upper()

    return inner


# Задекорируйте функцию calculate_tax
@uppercase
def calculate_tax(name, income, tax_rate):
    tax = income - income * (1 - tax_rate / 100)
    return f'{name} должен заплатить налог {tax}$'


print(calculate_tax("Ivan", 5000, 25))
print(calculate_tax("vaSilIy", 15000, 30))
print(calculate_tax("depardieu", 215000, 40))
