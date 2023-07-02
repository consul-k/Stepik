/*

Сравнение чисел
Напишите программу сравнивающие два целых числа.

Входные данные:
Два целых числа xx, yy

Выходные данные:
1 -- если x=yx=y
0 -- если x≠yx=y

Sample Input:

-2 2

Sample Output:

0

*/

#include <stdio.h>

int main() {
  int x,y;
  scanf("%d %d",&x,&y);
  
  switch (x==y) {
	case 0: printf("%d\n",0); break;
	case 1: printf("%d\n",1); break;
  }
  
  return 0;
}
