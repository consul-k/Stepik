/*

Напишите программу-калькулятор для четырёх основных арифметических действий.

Входные данные:
Символ действия cc и два целых числа aa, bb (b!=0)(b!=0)

Выходные данные:
Одно вещественное число, либо строку ERROR!, если введено недопустимое действие. Формат вывода чисел: два знака после запятой.

Sample Input:

+ 45 23

Sample Output:

68.00

*/

#include <stdio.h>
#include <locale.h>
int main(void) {
  setlocale(LC_ALL, "");

  char c;
  int a,b;
  double res;
  scanf("%c",&c);
  scanf("%d%d",&a,&b);

  switch (c) {
	default:  printf("ERROR!\n"); break;
    case '+' : printf("%.2lf\n",res = a + b) ; break;
    case '-' : printf("%.2lf\n",res = a - b) ; break;
    case '*' : printf("%.2lf\n",res = a * b); break;
    case '/' : printf("%.2lf\n",res = a / b) ; break;
  }

return (0);
}
