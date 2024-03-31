'''

Дан треугольник ABC на плоскости, заданный координатами своих вершин. Для этого треугольника вычислить:

    радиус вписанной в треугольник окружности;
    радиус описанной вокруг треугольника окружности;
    сумму длин трех медиан треугольника.

Формулы для вычислений

Радиус вписанной в треугольник окружности:

r=(p2−a)(p2−b)(p2−c)p2
r=2p​(2p​−a)(2p​−b)(2p​−c)​

​где a, b, c - длины сторон; p - периметр. 

Радиус описанной вокруг треугольника окружности:

R=a⋅b⋅c4⋅s
R=4⋅sa⋅b⋅c​где s - площадь треугольника.

Длины медиан треугольника:

Ma=12⋅2⋅(c2+b2)−a2
Ma​=21​⋅2⋅(c2+b2)−a2
​
Mb=12⋅2⋅(a2+c2)−b2
Mb​=21​⋅2⋅(a2+c2)−b2
​
Mc=12⋅2⋅(a2+b2)−c2
Mc​=21​⋅2⋅(a2+b2)−c2

​
Пояснения к реализации

    Для решения использовать шаблон (скопировать код в соответствующее окно среды разработки, после комментариев вставить необходимые операторы).
    Результаты вычислений (радиус вписанной окружности, радиус описанной окружности, сумму длин медиан) вывести без сообщений пользователю, 
    в одном операторе print, округлив значения до 4-х знаков после запятой.  
    Если по заданным точкам построить треугольник нельзя, вывести "error".

Входные данные:

    вещественное число (координата x точки А);
    вещественное число (координата y точки А);
    вещественное число (координата x точки B);
    вещественное число (координата y точки B);
    вещественное число (координата x точки C);
    вещественное число (координата y точки C).

Выходные данные:

    радиус вписанной окружности, радиус описанной окружности и сумма длин медиан или error. 
    Все значения округлить с указанной точностью, в операторе print никаких пояснений (текст в кавычках) не использовать.

Sample Input 1:

0
0
1
1
2
2

Sample Output 1:

error

Sample Input 2:

-12.8
3.4
-7.7
8.6
-14.6
-3.5

Sample Output 2:

0.9113 14.0042 22.8319

'''

from math import sqrt

def compute_len(x_0,y_0,x_1,y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())

a = compute_len(x_a,y_a,x_b,y_b)
b = compute_len(x_b,y_b,x_c,y_c)
c = compute_len(x_c,y_c,x_a,y_a)

if a+b<=c or b+c<=a or a+c<=b :
    print ("error")
else:
    p = ((a + b + c)/(2))
    s = sqrt((p * (p - a) * (p - b) * (p - c)))
    rv = round((sqrt((p-a) * (p-b) * (p-c) / p)),4)
    ro = round(((a*b*c)/(s*4)),4)
    summa = round(((0.5 * sqrt(2 * (c**2 + b**2) - a**2))+(0.5 * sqrt(2 * (c**2 + a**2) - b**2))+(0.5 * sqrt(2 * (a**2 + b**2) - c**2))),4)
    print(rv,ro,summa)
