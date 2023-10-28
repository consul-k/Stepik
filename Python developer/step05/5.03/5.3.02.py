'''

Вам дано целое неотрицательное число n. Нужно его перевернуть. Например, для числа 3214 нужно вывести 4123. 
Если вы переворачиваете число с нулями, и в обратной версии появляются незначащие нули, то их нужно убрать, например, для числа 100 ответом будет 1.

Sample Input 1:

3214

Sample Output 1:

4123

Sample Input 2:

0

Sample Output 2:

0

Sample Input 3:

1

Sample Output 3:

1

Sample Input 4:

12

Sample Output 4:

21

Sample Input 5:

100

Sample Output 5:

1

Sample Input 6:

102030

Sample Output 6:

30201

'''

print(int(input()[::-1]))  
