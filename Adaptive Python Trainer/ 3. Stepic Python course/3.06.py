'''

Напишите программу, которая выводит nn первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).

Формат ввода:
Строка, содержащая одно целое число nn, n>0n>0.

Формат вывода:
Строка, содержащая требуемую последовательность чисел, разделённых пробелом.

Sample Input:

7

Sample Output:

1 2 2 3 3 3 4

'''

n = int(input())
lst = [i for i in range(n+1) for j in range(i)]
print(*lst[:n])
