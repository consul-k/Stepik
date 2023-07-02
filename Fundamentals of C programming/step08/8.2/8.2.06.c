/*

Для заданной квадратной матрицы A[N] посчитать следующие величины:

    сумму элементов, находящихся над главной диагональю
    сумму элементов, расположенных под побочной диагональю


Входные данные:
Одно натуральное число NN. Далее с новой строки NN строк по NN целых чисел в каждой. NN не превышают десяти.

Выходные данные:
Два целых числа, записанных через пробел. Первым вывести меньшее из чисел.

Sample Input:

3
1 2 3
1 4 5
9 3 -7

Sample Output:

1 10

*/

#include <stdio.h>
 
int main()
{
    int n = 0, a = 0, b = 0;
    int i, j;
 
    do{
        scanf("%d", &n);
      
    }while(n < 1 || n > 10);
 
    int arr[n][n];
 
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            scanf("%d", &arr[i][j]);
            if(i < j) a += arr[i][j];
            if (i >= n - j) b += arr[i][j];
        }
    }
 
    
    (a < b) ? printf("%d %d", a, b) : printf("%d %d", b, a);
    printf("\n");
    return 0;
}
