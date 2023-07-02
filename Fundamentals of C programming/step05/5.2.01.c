/*

Определить является ли число чётным или нечётным.

Входные данные:
Одно целое положительное число kk. (0≤k≤100)(0≤k≤100)

Выходные данные:
Число 11, если kk -- чётное и −1−1, если kk -- нечётное.

Sample Input 1:

91

Sample Output 1:

-1

Sample Input 2:

0

Sample Output 2:

1

*/

#include <stdio.h>

int main() {
  int k;
  scanf("%d",&k);
  if (k%2==0)
  printf("1");
  else
  printf("-1");
    
  return 0;
}
