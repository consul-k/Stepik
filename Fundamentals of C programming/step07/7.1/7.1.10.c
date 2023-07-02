/*

Для заданного числа NN проверить, является ли оно простым.

Входные данные:
Одно натуральное число NN, отличное от 1.

Выходные данные:
1 -- если число простое
0 -- если число составное

Sample Input:

8

Sample Output:

0

*/

#include <stdio.h>

int main(void) {

  int n,c=0;
  scanf("%d",&n);
  
  for (int i = 1; i <= n; i++){
	if (n%i==0) {
		c = c + 1;
  		}
  }
  if (c==2)
  printf("\n%d",1);
  else
  printf("%d",0);
  
  return 0;
}
