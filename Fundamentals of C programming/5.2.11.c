/*

Идёт kk день года. Определить номер текущей недели в году. Предполагаем, что 1 января был понедельник.

Входные данные:
Целое число kk, 1≤k≤3651≤k≤365.

Выходные данные:
Одно целое число -- номер недели.

Sample Input 1:

12

Sample Output 1:

2

Sample Input 2:

243

Sample Output 2:

35

*/


#include <stdio.h>

int main(){
double k;
scanf("%lf",&k);
printf("%.lf\n", ceil(k/7));
return 0;
}
