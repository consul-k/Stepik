'''

Большой подвиг 3. В виде строки записано арифметическое выражение, например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть разным.

Необходимо выполнить вычисление и результат отобразить на экране. 
Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-), 
а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

Sample Input:

10+25 - 12

Sample Output:

23

'''

s = input().replace('+',' + ').replace('-',' - ').split()
res = 0
res += int(s[0])

for i,v in enumerate(s):
    if v == '+':
        res += int(s[i+1])
    elif v == '-':
        res -= int(s[i+1])
print(res)
