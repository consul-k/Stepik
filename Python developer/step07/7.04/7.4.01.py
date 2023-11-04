'''

Напишите программу, которая получает на ввод n строк, состоящих из двух слов разделенных пробелом, и выводит сгруппированные элементы по второму слову, и отсортированные по алфавиту. Разделите каждую группу при помощи строки <->.

Ввод:

n – количество строк

n строк состоящих из двух слов, разделенных пробелом.

Вывод:

Группы сформированные по второму слову, отсортированные по алфавиту и разделенные символом <->.

Sample Input 1:

5
Краснодар Россия
Амстердам Нидерланды
Москва Россия
Вашингтон США
Нью-Йорк США

Sample Output 1:

Нидерланды Амстердам
<->
Россия Краснодар
Россия Москва
<->
США Вашингтон
США Нью-Йорк

Sample Input 2:

1
a b

Sample Output 2:

b a

Sample Input 3:

2
a b
b b

Sample Output 3:

b a
b b

Sample Input 4:

3
a b
b b
b a

Sample Output 4:

a b
<->
b a
b b

Sample Input 5:

3
a b
b c
c d

Sample Output 5:

b a
<->
c b
<->
d c

Sample Input 6:

3
c d
b c
a b

Sample Output 6:

b a
<->
c b
<->
d c

'''

d = {}
for i, j in [input().split() for string in range(int(input()))]:
    d.setdefault(j, []).append(i)

print(*['\n'.join([f'{k} {v}' for v in sorted(vs)]) for k, vs in sorted(d.items())], sep='\n<->\n')
