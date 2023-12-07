'''

В скором времени в Берляндии откроется новая почтовая служба "Берляндеск". Администрация сайта хочет запустить свой проект как можно быстрее, 
поэтому они попросили Вас о помощи. Вам предлагается реализовать прототип системы регистрации сайта.

Система должна работать по следующему принципу. Каждый раз, когда новый пользователь хочет зарегистрироваться, 
он посылает системе запрос name со своим именем. Если данное имя не содержится в базе данных системы, 
то оно заносится туда и пользователю возвращается ответ OK, подтверждающий успешную регистрацию. 
Если же на сайте уже присутствует пользователь с именем name, то система формирует новое имя и выдает его пользователю в качестве подсказки,
при этом подсказка также добавляется в базу данных. Новое имя формируется по следующему правилу. 
К name последовательно приписываются числа, начиная с единицы (name1, name2, ...), и среди них находят такое наименьшее i, 
что namei не содержится в базе данных сайта.

Входные данные

В первой строке входных данных задано число n (1 ≤ n ≤ 105). Следующие n строк содержат запросы к системе. 
Каждый запрос представляет собой непустую строку длиной не более 32 символов, состоящую только из строчных букв латинского алфавита.

Выходные данные

В выходных данных должно содержаться n строк — ответы системы на запросы: OK в случае успешной регистрации, или подсказку с новым именем, 
если запрашиваемое уже занято.

Sample Input 1:

4
abc
abcd
abc
acab

Sample Output 1:

OK
OK
abc1
OK

Sample Input 2:

3
b
b
b

Sample Output 2:

OK
b1
b2

Sample Input 3:

3
vhn
vhn
h

Sample Output 3:

OK
vhn1
OK

Sample Input 4:

4
d
hd
d
h

Sample Output 4:

OK
OK
d1
OK

Sample Input 5:

10
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp
bhnqaptmp

Sample Output 5:

OK
bhnqaptmp1
bhnqaptmp2
bhnqaptmp3
bhnqaptmp4
bhnqaptmp5
bhnqaptmp6
bhnqaptmp7
bhnqaptmp8
bhnqaptmp9

Sample Input 6:

10
fpqhfouqdldravpjttarh
fpqhfouqdldravpjttarh
fpqhfouqdldravpjttarh
fpqhfouqdldravpjttarh
fpqhfouqdldravpjttarh
fpqhfouqdldravpjttarh
jmvlplnrmba
fpqhfouqdldravpjttarh
jmvlplnrmba
fpqhfouqdldravpjttarh

Sample Output 6:

OK
fpqhfouqdldravpjttarh1
fpqhfouqdldravpjttarh2
fpqhfouqdldravpjttarh3
fpqhfouqdldravpjttarh4
fpqhfouqdldravpjttarh5
OK
fpqhfouqdldravpjttarh6
jmvlplnrmba1
fpqhfouqdldravpjttarh7

'''

n = int(input())
s = {}
for i in range(1,n+1):
    if (a := input()) not in s:
        print('OK')
        s[a] = 1
    else:
        print(a + str(s[a]))
        s[a] = s[a] + 1
