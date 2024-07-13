# объявление функции
def number_of_factors(num):
    res = 1
    for i in range(2,num+1):
        if num%i==0:
            res += 1
    return res
# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
