/*

Составьте программу подсчёта размера оплаты за электроэнергию по показаниями счётчика и тарифу. На вход поступают 3 числа.
Первое число -- целое число. Показания счётчика в кВт*ч на начало месяца.
Второе число -- целое число. Показания счётчика в кВт*ч на конец месяца.
Третье число -- вещественное число. Стоимость одного кВт*ч в рублях.

Программа должны вывести на экран размер оплаты за электроэнергию. Результат выведите с двумя знаками после запятой.

Sample Input:

1200 1400 0.2

Sample Output:

40.00

*/

#include <stdio.h>
int main() {
  int a, b;
  double c, summa;
  scanf("%d",&a);
  scanf("%d",&b);
  scanf("%lf",&c);

  summa = (b-a)*c;
  printf("%.2lf\n",summa);

  return 0;
}
