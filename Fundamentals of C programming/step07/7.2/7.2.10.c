/*

Дано натуральное число NN. Найти наименьшее натуральное число rr, такое, что 2r≥N2r≥N.

Входные данные:
Одно натуральное число NN.

Выходные данные:
Число rr.

Sample Input 1:

128

Sample Output 1:

7

Sample Input 2:

1

Sample Output 2:

1

Sample Input 3:

7

Sample Output 3:

3

*/

#include <stdio.h>
#include <math.h>

int main() {

  int n,p=1,k=1;
  scanf("%d",&n);

  while (k<n) {
	p++;
	k = pow(2,p);
    }

  printf("%d\n",p);
  
  return 0;
}
