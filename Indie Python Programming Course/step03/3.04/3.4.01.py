'''

Классическая задача для начинающих. 

Ваша программа должна считать одно натуральное число, после чего вывести:

    “Fizz”, если это число делится на 3;
    “Buzz”, если это число делится на 5;
    “FizzBuzz”, если выполнены оба предыдущих условия;
    само это число в остальных случаях.

Sample Input 1:

15

Sample Output 1:

FizzBuzz

Sample Input 2:

10

Sample Output 2:

Buzz

Sample Input 3:

12

Sample Output 3:

Fizz

Sample Input 4:

13

Sample Output 4:

13

'''

a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)
