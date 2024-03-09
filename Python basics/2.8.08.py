'''

Нарисуйте с помощью знаков  * и - ёлочку . Вводные данные - ширина основания ёлочки. Вводим 5, в консоль выводится: 

--*--
-***-
***** , где количество знаков * на первом уровне = 5.

Вводное число нечетное.

Sample Input:

7

Sample Output:

---*---
--***--
-*****-
*******

'''

width = int(input())

for i in range(width//2 + 1):
    for j in range(width//2 - i):
        print("-", end="")
    for k in range(2*i + 1):
        print("*", end="")
    for j in range(width//2 - i):
        print("-", end="")
    print()
