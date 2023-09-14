'''

На вход программе подаётся целое число. Выведите в консоль строку вида: a * a = b, где a - полученное число, а b - результат произведения числа a на само себя.

Sample Input 1:

1

Sample Output 1:

1 * 1 = 1

Sample Input 2:

100

Sample Output 2:

100 * 100 = 10000

Sample Input 3:

5

Sample Output 3:

5 * 5 = 25

Sample Input 4:

36

Sample Output 4:

36 * 36 = 1296

'''

a = int(input())
print(f'{a} * {a} = {a*a}')
