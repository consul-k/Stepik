/*

Написать программу проверяющую, является ли правильной дробь ABBA​.

Входные данные:
Два натуральных числа A,BA,B.

Выходные данные:
Строка yes, если дробь правильная, строка no в противном случае.

Sample Input:

84 47

Sample Output:

no

*/

#include <stdio.h>

int main() {
  int a,b;
  scanf("%d %d",&a,&b);
    
  if (a<b) {
      printf("yes\n");
  } else 
  printf("no\n");
    
  return 0;
}
