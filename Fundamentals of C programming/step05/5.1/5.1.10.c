/*

Побитовая инверсия
Напишите программу, которая осуществляет инверсию однобитного числа (0 или 1).

Входные данные:
Число KK либо 00, либо 11.

Выходные данные:
Вывести 11, если K=0K=0
вывести 00, если K=1K=1

Sample Input 1:

0

Sample Output 1:

1

Sample Input 2:

1

Sample Output 2:

0

*/

#include <stdio.h>

int main() {
  int a, number;
  scanf("%d",&a);

  number = (a+1)%2;
  printf("%d\n",number);

  return 0;
}
