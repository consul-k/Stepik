'''

Дано дробное число x. Выведите вторую цифру после точки.

Sample Input 1:

1.2345

Sample Output 1:

3

Sample Input 2:

1.005

Sample Output 2:

0

Sample Input 3:

3.913333

Sample Output 3:

1

Sample Input 4:

333333.962222

Sample Output 4:

6

Sample Input 5:

444343459.99999

Sample Output 5:

9

Sample Input 6:

123.555

Sample Output 6:

5

Sample Input 7:

-123.478

Sample Output 7:

7

'''

x = float(input())
print(int((abs(x)*100)%10))
