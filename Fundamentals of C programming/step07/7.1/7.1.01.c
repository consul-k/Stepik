/*

Написать программу выводящую на экран первые NN натуральных чисел.

Входные данные:
Одно  целое число NN, N>0N>0

Выходные данные:
Первые NN натуральных чисел, записанных через пробел.

Sample Input:

8

Sample Output:

1 2 3 4 5 6 7 8

*/

#include <stdio.h>

int main(void) {

  int n = 0;
  scanf("%d", &n);
  
  for (int i = 1; i <= n; i++){
    printf("%d ",i);
  }

  return 0;
}
