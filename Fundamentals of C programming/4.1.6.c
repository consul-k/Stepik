/*

Напишите программу, определяющую нечётные числа.

На вход программы поступает одно целое неотрицательное число. Программа должна вывести 1, если число нечётное, и 0, если число чётное.

Sample Input:

2

Sample Output:

0

*/

#include <stdio.h>
int main() {
  int a, number;
  scanf("%d",&a);

  number = a%2;
  printf("%d\n",number);

  return 0;
}
