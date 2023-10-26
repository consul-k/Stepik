'''

Вам требуется подобрать коробку, для вашего товара. Известно, что ширина, высота и глубина коробки – целые числа.

Вашей программе даются на вход 3 числа с плавающей точкой – ширина, высота и глубина товара. Вам требуется подобрать для этого товара коробку. 
Выведите ширину, высоту и глубину коробки.

Sample Input 1:

8.4
6.3
2.9

Sample Output 1:

9
7
3

Sample Input 2:

1.0
2.0
3.0

Sample Output 2:

1
2
3

Sample Input 3:

1.01
2.003
4.006

Sample Output 3:

2
3
5

'''

import math

a, b, c = float(input()), float(input()), float(input())
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))
