/*

Написать программу, позволяющую получить словесное описание школьных отметок (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).

Входные данные: Одно целое число kk от 1 до 5.

Выходные данные:
Соответствующая kk текстовое описание отметки.

Sample Input:

3

Sample Output:

удовлетворительно

*/

#include <stdio.h>
#include <locale.h>
int main(void) {
  setlocale(LC_ALL, "");
  char s;  
  scanf("%c",&s);

  switch (s) {
    default  : break;
    case '1' : printf("плохо\n"); break;
    case '2' : printf("неудовлетворительно\n"); break;
    case '3' : printf("удовлетворительно\n"); break;
	case '4' : printf("хорошо\n"); break;
	case '5' : printf("отлично\n"); break;
  }

  return 0;
}
