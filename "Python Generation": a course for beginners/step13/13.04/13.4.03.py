# объявление функции
def get_factors(num):
    res = [1]
    for i in range(2,num+1):
        if num%i==0:
            res.append(i)
    return res

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
