/*

Вычислить номер дня в невисокосном году по заданным числу и месяцу.

Входные данные:
Два целых числа. Первое число mm -- номер месяца. 1≤m≤121≤m≤12
Второе число dd -- номер дня в месяце. 1≤d≤311≤d≤31

Выходные данные:
Одно целое число -- порядковый номер дня в невисокосном году.

Sample Input 1:

2 4

Sample Output 1:

35

Sample Input 2:

6 12

Sample Output 2:

163

*/

#include <stdio.h>

int main(void) {
  int m, d, m1 = 31, m2 = 28, m3 = 30, day;
  scanf("%d %d",&m,&d);

  switch (m) {
	case 1: day = 0; break;
    case 2: day = m1 + d; break;
    case 3: day = m1 + m2 + d; break;
    case 4: day = m1*2 + m2 + d; break;
    case 5: day = m1*2 + m2 + m3 + d; break;
    case 6: day = m1*3 + m2 + m3 + d; break;
    case 7: day = m1*3 + m2 + m3*2 + d; break;
    case 8: day = m1*4 + m2 + m3*2 + d; break;
    case 9: day = m1*5 + m2 + m3*2 + d; break;
    case 10: day = m1*5 + m2 + m3*3 + d; break;
    case 11: day = m1*6 + m2 + m3*3 + d; break;
    case 12: day = m1*6 + m2 + m3*4 + d; break;
  }

  printf("%d\n",day);
  return 0;
}
