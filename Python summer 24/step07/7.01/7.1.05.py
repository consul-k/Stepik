# объявление функции
def print_digit_sum(num):
    res = 0
    for i in str(num):
        res += int(i)
    print(res)
    
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
