'''

Напишите программу, которая  принимает на вход три целых числа в одной строке через пробел и выводит их последовательно через запятую как в примерах ниже

Sample Input 1:

1 2 3

Sample Output 1:

1,2,3

Sample Input 2:

5 43 21

Sample Output 2:

5,43,21

Sample Input 3:

8 7 -90

Sample Output 3:

8,7,-90

Sample Input 4:

5 4 3

Sample Output 4:

5,4,3

'''

a,b,c = map(int, input().split())
print(a,b,c,sep=',')
