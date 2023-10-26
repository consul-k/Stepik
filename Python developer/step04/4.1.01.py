'''

Ваша программа принимает целое число n. 
Напишите программу, определяющую что число находится в интервале от 5 включительно до 10 строго или от 101 строго до 200 включительно 
или иными словами n∈[5,10)∪(101,200]n∈[5,10)∪(101,200]. В качестве ответа выведите True если находится и False если не находится.

Sample Input 1:

5

Sample Output 1:

True

Sample Input 2:

10

Sample Output 2:

False

Sample Input 3:

7

Sample Output 3:

True

Sample Input 4:

101

Sample Output 4:

False

Sample Input 5:

200

Sample Output 5:

True

'''

a = int(input())
print(5<=a<10 or 101<a<=200)
