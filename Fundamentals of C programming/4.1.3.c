/*

На вход программы поступает целое трёхзначное число. Напишите программу, которая выводит сумму цифр этого числа.

Sample Input:

123

Sample Output:

6

*/

#include <stdio.h>
int main() {
  int a;
  scanf("%d", &a);
  printf("%d", a%10+a/10%10+a/100);
}
