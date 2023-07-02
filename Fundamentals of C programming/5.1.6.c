/*

Даны натуральные числа MM и NN. Вывести младшую цифру целой части и старшую цифру дробной части числа MNNM​.

Входные данные:
Два натуральных числа MM и NN, записанных через пробел.

Выходные данные:
Два целых числа.  Первое −− младшая цифра целой части числа MNNM​, второе −− старшая цифра дробной части числа MNNM​

Sample Input 1:

1554 155

Sample Output 1:

0 0

Sample Input 2:

1234 473

Sample Output 2:

2 6

*/

#include <stdio.h>
 
int main()
{
    double x, z; int n, m;
    scanf("%i", &n);
    scanf("%i", &m);
    x = (double)n/m;
    z = x-(int)x;
    printf("%i %i\n", (int)x%10, (int)(z*10));
    return 0;
}
