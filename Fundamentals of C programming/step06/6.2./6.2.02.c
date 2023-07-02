/*

Квадранты.
На координатной плоскости OxyOxy​ задана точка A(x,y)A(x,y). 
Необходимо указать квадрант, в котором она расположена. Номера квадрантов представлены на рисунке ниже.
https://ucarecdn.com/d1aa75d1-cadc-4d5d-bce3-ba1df8ce7798/

Входные данные:
Два вещественных числа xx, yy, которые не равны нулю.

Выходные данные:
Вывести одно целое -- номер квадранта.

Sample Input:

2 -4

Sample Output:

4

*/

#include <stdio.h>

int main() {
  double x, y;
  scanf("%lf %lf", &x, &y);
  switch(x>0) {
      case 1: switch(y>0) {
          case 1: printf("1"); break;
          case 0: printf("4"); break;
      } break;
      case 0: switch(y>0) {
          case 1: printf("2"); break;
          case 0: printf("3"); break;
      } break;
  }
  return 0;
}
