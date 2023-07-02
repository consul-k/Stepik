/*

Степень двойки
По данном числу NN определить, является ли оно степенью числа 22.

Входные данные:
Одно целое неотрицательное число NN.

Выходные данные:
YES -- если число NN является степенью двойки, и NO в противном случае.

Sample Input:

128

Sample Output:

YES

*/

#include <stdio.h>
#include <math.h>

int main(void) {

  int n,a=0,k=0;
  scanf("%d", &n);

  while(a < n && n!=0){
    a = pow(2,k);
	k++;
  }
	if (a==n && n!=0)
		printf("YES\n");
	else
		printf("NO\n");

  return 0;
}
