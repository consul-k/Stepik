'''

На вход программе поступает строка, состоящая из нескольких слов, знаком разделителем между словами будем считать символ пробела. 
Ваша задача исключить из строки дублирующие слова: первое появление слова остается в строке, второе и все последующие появления исключаются. 
При сравнении на дубли строк регистр букв не учитывать, это значит слова python и PyThOn считаются одинаковыми.

В качестве ответа необходимо вывести итоговую строку без дублей.

Sample Input 1:

Python is best I love python

Sample Output 1:

Python is best I love

Sample Input 2:

one one two two three four four five six six one two three four five six

Sample Output 2:

one two three four five six

Sample Input 3:

Two one One SIX two thrEE four four five SIX six one two three four five six ONE

Sample Output 3:

Two one SIX thrEE four five

'''

x = list(map(str, input().split()))
res = []
result = []
for c in x:
    if c.lower() not in res:
        res.append(c.lower())
        result.append(c)
print(*result)
