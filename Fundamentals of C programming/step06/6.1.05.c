/*

Усовершенствуйте программу, написанную на прошлом шаге. Теперь она должна работать для любых целых чисел, включая случай, когда b=0b=0.

Входные данные:
Два целых числа aa, bb и символ действия cc.

Выходные данные:
Одно вещественное число, либо строку ERROR!, если введено недопустимое действие или действие выполнить невозможно. Формат вывода чисел: два знака после запятой.

Подсказки:
используйте вложенный оператор switch

Sample Input:

45 23 +

Sample Output:

68.00

*/

#include <stdio.h>
#include <locale.h>
int main(void) {
  setlocale(LC_ALL, "");
  char c;
  int a,b;
  scanf("%d %d %c",&a,&b,&c);

  switch (c) {
	default: printf("ERROR!\n"); break;
    case '+' : printf("%.2lf\n",(double)a + b); break;
    case '-' : printf("%.2lf\n",(double)a - b); break;
    case '*' : printf("%.2lf\n",(double)a * b); break;
    case '/' :
		switch (b) {
		  case 0: printf("ERROR!\n"); break;
	      default: printf("%.2lf\n",(double)a / b); break;
	    }
  }
	return 0;
}
