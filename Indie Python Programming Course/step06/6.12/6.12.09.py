'''

Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать.
Входные данные

Программа получает на вход строку, состоящую из заглавных и строчных символов, цифр и знаков препинания.
Выходные данные

Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.

Sample Input 1:

hello_world!

Sample Output 1:

helo_wrd!

Sample Input 2:

abc312re542Ab

Sample Output 2:

abc312re54A

Sample Input 3:

123454321123

Sample Output 3:

12345

Sample Input 4:

qqqqqqqqqqqqqqq

Sample Output 4:

q

'''

s = input()
s1 = set(s)
for i in s:
    if i in s1:
        print(i,end='')
        s1.discard(i)
