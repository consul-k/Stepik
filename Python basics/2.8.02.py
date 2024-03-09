'''

Найти площади фигур (прямоугольник, треугольник, круг)

Ввод: 
1)название фигуры
2) радиус(если круг)

2) a
3) b (если прямоугольник)

2) a
3) b 
4) c (если треугольник) можно считать по формуле Герона: корень из (p(p−a)(p−b)(p−c))

 

Примечание:
• ответ при расчете всех фигур в типе данных float;
• число pi упрощенное = 3.14

Sample Input:

треугольник
3
4
5

Sample Output:

6.0

'''

import math

shape = input()

if shape == "круг":
    radius = float(input())
    area = 3.14 * radius**2
elif shape == "прямоугольник":
    a = float(input())
    b = float(input())
    area = a * b
elif shape == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(area)
