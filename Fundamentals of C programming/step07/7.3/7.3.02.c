/*

Пирамида.
Вывести на экран пирамиду из чисел (см. пример входных данных).

Входные данные:
Одно целое число NN.

Выходные данные:
Пирамида из натуральных чисел высоты NN.

Sample Input 1:

5

Sample Output 1:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Sample Input 2:

1

Sample Output 2:

1 

*/

#include <stdio.h>

int main() {
    int n, i, j;
    scanf("%d", &n);
    for (i = 1; i <= n; i++){
        for (j = 1; j <= i; j++) {
            printf("%d ", j) ;
        }
        printf("\n") ;
    }
    return 0;
}
