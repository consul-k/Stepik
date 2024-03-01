/*

На JavaScript можно писать в Python стиле -- без точек с запятыми, без let, с привычными фунциями.

На этом курсе можно использовать привычные методы Питона, но, конечно, с особенностями и ограничениями JavaScript.

Попробуйте их здесь. Это песочница для Python, принимаются любые ответы. Доступны привычные функции -- input, print, int, str, float, max, min, abs, round, range, sum.

Sample Input:

World

Sample Output:

*/

// input / print
name = input()
print("Hello", name)

// int / float / str
a = float("25.5")
b = int(25.5)
c = str(25.5)
d = abs(-25.5)
e = round(25.5)

// for in range
for (i of range(10))
  print(i)

// max min
print(max([1, 2, 7, -3, 5]))
print(min([1, 2, 7, -3, 5]))

// sum
print(sum([1, 2, 7, -3, 5]))
