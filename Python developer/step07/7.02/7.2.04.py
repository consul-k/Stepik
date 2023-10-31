'''

Вам дана строка из слов, разделенных пробелами. Посчитайте для каждого слова – сколько оно раз встречалась в тексте.

Ввод:

s – строка, разделенная пробелами

Вывод:

key ,res – где key – слово, а res – количество раз, сколько оно встретилось в строке. Ключи отсортируйте в алфавитном порядке

Sample Input 1:

a b a a c c d b

Sample Output 1:

a 3
b 2
c 2
d 1

Sample Input 2:

a

Sample Output 2:

a 1

Sample Input 3:

a b

Sample Output 3:

a 1
b 1

Sample Input 4:

aaa

Sample Output 4:

aaa 1

Sample Input 5:

a a a

Sample Output 5:

a 3

Sample Input 6:

a b b a

Sample Output 6:

a 2
b 2

Sample Input 7:

d c b a a a

Sample Output 7:

a 3
b 1
c 1
d 1

'''

s = [i for i in input().split()]
d = dict()

for char in s:
    if not d.get(char):
        d[char] = 0
    d[char] = s.count(char)
    
for key, value in sorted(d.items()):
    print("{0} {1}".format(key,value))
