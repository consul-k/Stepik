/*

Количество цифр
Подсчитать количество цифр в записи натурального числа NN.

Входные данные:
Одно натуральное число NN.

Выходные данные:
Одно целое число kk -- количество цифр в записи числа NN.

Sample Input:

12938

Sample Output:

5

*/

#include <stdio.h>
#include <stdlib.h>

int main() {

  int n,count=0;
  scanf("%d",&n);

  while (n>0) {
	n = n / 10;
	count++;
    }

  printf("%d\n",count);
  return 0;
}
