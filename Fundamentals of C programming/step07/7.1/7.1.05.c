/*

Факториал.
Для целого числа k(0≤k≤12)k(0≤k≤12) посчитать k!k!.

Входные данные:
Одно целое число kk, (0≤k≤12)(0≤k≤12).

Выходные данные:
Значение факториала числа kk.

Sample Input:

4

Sample Output:

24

*/

#include <stdio.h>

int main(void) {

  int k,f=1;
  scanf("%d",&k);
  
  for (int i = 1; i <= k; i++){
	f = f*i;
  }
  printf("%d\n",f);

  return 0;
}
