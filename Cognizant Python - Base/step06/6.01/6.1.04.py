# создайте вашу функцию:
def super_sum(*args):
    return sum(args)

# ваша функция будет использована вот так:
num1 = super_sum(1, 2, 3)  # 6
num2 = super_sum(10, 20, 30, 40)  # 100
num3 = super_sum(100, 200, 300, 400, 500)  # 1500
num4 = super_sum()  # 0

# результат: print(num1 + num2 + num3 + num4)  # 1606
