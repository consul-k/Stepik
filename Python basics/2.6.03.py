'''

1) Создайте пустой список с возможностью его заполнения с клавиатуры через функцию extend.
2) Выведите в консоль первые 3 символа, начиная со второго символа включчительно.

Sample Input:

крот

Sample Output:

['р', 'о', 'т']

'''

a = []
a.extend(input())
print(a[1:4:])
