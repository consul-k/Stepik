'''

Посчитайте факториал числа n! по формуле ниже:

n!=1∗2∗3∗4∗...∗nn!=1∗2∗3∗4∗...∗n

Например для входного числа 5 алгоритм расчета следующий:

5!=1∗2∗3∗4∗5=1205!=1∗2∗3∗4∗5=120

Sample Input 1:

5

Sample Output 1:

120

Sample Input 2:

0

Sample Output 2:

1

Sample Input 3:

1

Sample Output 3:

1

Sample Input 4:

2

Sample Output 4:

2

'''

s = 1
for i in range(1,int(input())+1):
    s*=i
print(s)
