'''

Напишите программу, которая получает на вход целое число n и выводит 5 строк содержащих True или False с ответами на эти вопросы:

1) Является ли число четным?

2) Число является положительным?

3) Число находится в промежутке от -5 включительно до 5 включительно?

4) Число делится на 3 и 4, но не делится на 7?

5) Является ли число трехзначным?

Sample Input 1:

5

Sample Output 1:

False
True
True
False
False

Sample Input 2:

100

Sample Output 2:

True
True
False
False
True

Sample Input 3:

84

Sample Output 3:

True
True
False
False
False

Sample Input 4:

-5

Sample Output 4:

False
False
True
False
False

Sample Input 5:

12

Sample Output 5:

True
True
False
True
False

Sample Input 6:

999

Sample Output 6:

False
True
False
False
True

Sample Input 7:

1001

Sample Output 7:

False
True
False
False
False

Sample Input 8:

-100

Sample Output 8:

True
False
False
False
True

'''

n = int(input())
print(n%2==0)
print(n>0)
print(-5<=n<=5)
print(n%3==0 and n%4==0 and n%7!=0)
print(-999<=n<=-100 or 100<=n<=999)
