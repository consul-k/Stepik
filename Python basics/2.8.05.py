'''

Напишите программу, которая получает на 
вход три целых числа, по одному числу в
строке, и выводит на консоль в три строки
сначала максимальное, потом минимальное,
после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

Sample Input:

3
8
4

Sample Output:

8
3
4

'''

a = int(input())
b = int(input())
c = int(input())
lst = [a,b,c]
max_n = max(lst)
min_n = min(lst)
lst.remove(max_n)
lst.remove(min_n)
print(max_n)
print(min_n)
print(*lst)
