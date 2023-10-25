'''

Представим, что вы разработчик серверных приложений. У вас есть потребность в измерении количества времени, которое проводят ваши пользователи на сайте. 
Фронтенд посылает вам время в минутах, которое пользователь провел на сайте. Вам в ответ нужно узнать сколько в этих минутах часов и минут.

Или иными словами: 

Ваша программа принимает одну переменную m – количество минут, которое пользователь провел на сайте. Вам нужно определить сколько в этих минутах часов и оставшихся минут.

Sample Input 1:

153

Sample Output 1:

2 33

Sample Input 2:

90

Sample Output 2:

1 30

Sample Input 3:

60

Sample Output 3:

1 0

Sample Input 4:

0

Sample Output 4:

0 0

Sample Input 5:

156

Sample Output 5:

2 36

'''

m = int(input())
print(m//60,m%60)
