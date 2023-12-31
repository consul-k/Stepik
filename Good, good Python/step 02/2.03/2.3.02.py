'''

Подвиг 2. Допишите текст программы для нахождения минимального значения из пяти введенных целых чисел с выводом результата в консоль с помощью функции print.

Sample Input:

8 11 -5 3 0

Sample Output:

-5

'''

numbers = list(map(int, input().split()))
print(min(numbers))
