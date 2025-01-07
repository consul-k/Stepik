def super_minus(**kwargs):
    result = 0
    super_plus_val = kwargs.get('super_plus', 0)
    first_num = True

    for key, value in kwargs.items():
      if key == 'super_plus':
        result += value
        continue
      if first_num:
        result += value
        first_num = False
        continue
      result -= value

    return result


num1 = super_minus(n1=10, n2=2, n3=5)  # 10-2-5 = 3
num2 = super_minus(n1=100, n2=20, n3=50, n4=10, n5=10, n6=5)  # 100-20-50-10-10-5 = 5
num3 = super_minus(super_plus=500, n1=100, n2=300, n3=200)  # 500+100-300-200 = 100
num4 = super_minus()  # 0

# результат: print(num1 + num2 + num3 + num4)  # 108
