/*

Дубликаты
Удалить из последовательности дубликаты.

Входные данные:
В первой строке задано натуральное число NN. Во второй строке записана упорядоченная по возрастанию последовательность из NN целых чисел, которая может содержать одинаковые элементы.

Выходные данные:
Вывести все различные элементы последовательности, упорядоченные по возрастанию.

Sample Input 1:

21
 -2 -2 -2 4 5 6 7 7 7 7 7 7 7 7 91 91 92 92 93 93 96

Sample Output 1:

-2 4 5 6 7 91 92 93 96

Sample Input 2:

9
 1 2 4 5 6 7 8 9 10

Sample Output 2:

1 2 4 5 6 7 8 9 10

Sample Input 3:

1
 -7

Sample Output 3:

-7

*/

#include <stdio.h>
 
int main() {
int a, b,x=-9999;
scanf("%d", &a);
for (int i=0 ;  i <= (a-1); i++){
scanf("%d", &b);
 if(b > x)
printf("%d ", b );   
x=b;
}
  return 0;
}
