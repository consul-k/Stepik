'''

Ваша программа получает на вход целое число n. В случае если оно четное – прибавьте к нему 10, а если нечетное отнимите 10.

В качестве вывода ваша программа должна выдать результат вычислений.

Sample Input 1:

10

Sample Output 1:

20

Sample Input 2:

9

Sample Output 2:

-1

Sample Input 3:

0

Sample Output 3:

10

'''

n = int(input())
if n%2==0:
    print(n+10)
else:
    print(n-10)
