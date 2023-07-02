/*

Даны три числа. Подсчитать количество положительных среди этих чисел.

Входные данные:
Три целых числа a,b,ca,b,c.

Выходные данные:
Одно целое число -- количество положительных чисел, среди чисел a,b,ca,b,c.

Sample Input:

79 -18 88

Sample Output:

2

*/

#include <stdio.h>

int main() {
  int a,b,c,count=0;
  scanf("%d %d %d",&a,&b,&c);
  
  if (a > 2) {
    count = count+1;
 } if (b > 2) {
   count = count+1;
 } if (c > 2) {
   count = count+1;
 }

 printf("%d\n",count);

  return 0;
}
