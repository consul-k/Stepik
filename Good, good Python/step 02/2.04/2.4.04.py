'''

Подвиг 4. Допишите программу, в которой вводятся два слова (в переменные s1 и s2) в одну строчку через пробел, и отображаются в консоли в формате:

Word 1: s1 | Word 2: s2

Sample Input:

I love

Sample Output:

Word 1: I | Word 2: love

'''

s1, s2 = map(str.strip, input().split())
print(f'Word 1: {s1} | Word 2: {s2}')
