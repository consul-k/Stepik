/*

Определить, является ли целое число чётным или нечётным.

Входные данные:
Одно целое число k. (−100≤k≤100)(−100≤k≤100)

Выходные данные:
Число 11, если kk -- чётное, и −1−1, если kk -- нечётное.

Sample Input 1:

2

Sample Output 1:

1

Sample Input 2:

-2

Sample Output 2:

1

*/

#include <stdio.h>

int main() {
  int k;
  scanf("%d",&k);
  if (k%2==0||k==0)
  printf("1");
  else
  printf("-1");
    
  return 0;
}
