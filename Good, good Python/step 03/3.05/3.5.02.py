'''

Подвиг 2. Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел.
С помощью метода format, используя ключи в качестве имен переменных, сформировать строку: "Габариты: <ширина> x <глубина> x <высота>". 
Результат вывести на экран.

Sample Input:

8 11 13

Sample Output:

Габариты: 8 x 11 x 13

'''

a, b, c = map(int, input().split())
print(f'Габариты: {a} x {b} x {c}')
