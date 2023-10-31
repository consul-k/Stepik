'''

Вам дана последовательность чисел заканчивающаяся -1. Выведете ее в обратном порядке без учета -1.

Ввод:

Последовательность чисел

Вывод:

Последовательность чисел в обратном порядке.

Sample Input 1:

1
2
3
4
-1

Sample Output 1:

4
3
2
1

Sample Input 2:

1
1
1
-1

Sample Output 2:

1
1
1

Sample Input 3:

-1

Sample Output 3:

Sample Input 4:

1
2
2
3
3
4
4
5
-1

Sample Output 4:

5
4
4
3
3
2
2
1

'''

stack = []
element = int(input())

while element != -1:
    stack.append(element)
    element = int(input())

for i in reversed(stack):
    print(i)
