/*

По заданному числу N сформировать матрицу (N×NN×N) следующего вида:


1    2    3   ...  n-2  n-1  n
2    1    2   ...  n-3  n-2  n-1
3    2    1   ...  n-4  n-3  n-2
...              ...
n-1  n-2  n-3 ...  2    1    2
n    n-1  n-2 ...  3    2    1

Входные данные:
Одно натуральное число NN.

Выходные данные:
Вывести на экран массив NN на NN, указанного вида. Числа разделять пробелами.

Sample Input:

4

Sample Output:

1 2 3 4
2 1 2 3
3 2 1 2
4 3 2 1

*/

#include <stdio.h>

int main() {
      int i,j,k,n,*a,*b;
    
    scanf("%d",&n);
    a=(int*)malloc(n*n*sizeof(int));
    for(b=a,i=0; i<n; i++,b+=n)
    {
        for(j=0,k=i+1; j<i; j++,k--) b[j]=k;
        for(k=1; j<n; j++,k++) b[j]=k;
    }
    for(i=0; i<n; i++,printf("\n"))
        for(j=0; j<n; j++)
            printf("%3d",a[i*n+j]);
    free(a);
  return 0;
}
