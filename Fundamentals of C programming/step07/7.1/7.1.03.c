/*

Усовершенствовать программу, написанную на прошлом шаге: дополнительно на отдельной строке вывести количество напечатанных чисел.

Входные данные:
Два целых числа K,MK,M. При этом MM больше KK.

Выходные данные:
Натуральные числа в порядке возрастания, принадлежащие промежутку [K,M][K,M]. Числа нужно разделять одним пробелом.
На новой строке вывести количество выведенных натуральных чисел, а если натуральные числа отсутствуют -- ноль.

Уточнение:

На конце первой строки обязательно должен ставиться пробел.

Sample Input 1:

3 12

Sample Output 1:

3 4 5 6 7 8 9 10 11 12 
10

Sample Input 2:

-3 3

Sample Output 2:

1 2 3 
3

*/

#include <stdio.h>

int main(void) {

  int k,m,count=0;
  scanf("%d %d",&k,&m);
  
  for (int i = k; i <= m; i++){
	if (i>0) {
	count++;
    printf("%d ",i);
    }
  }

  printf("\n%d\n",count);

  return 0;
}
