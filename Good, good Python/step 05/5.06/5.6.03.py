'''

Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n). 
Результат вывести на экран в строчку через пробел.

Sample Input:

11

Sample Output:

2 3 5 7

'''

n = int(input())
 
for k in range(2, n):
    prime = True
    for i in range(2, k):
        if k%i == 0:
            prime = False
            break
    if prime:
        print(k, end=' ')
