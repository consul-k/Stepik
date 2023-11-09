'''

Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза.
Для удобства будем считать словом любую последовательность символов.

Sample Input 1:

Hello my friend

Sample Output 1:

3

Sample Input 2:

Золотистый ретривер

Sample Output 2:

2

Sample Input 3:

aa bbb ccc dddd

Sample Output 3:

4

'''

a = input().split()
print(len(a))
