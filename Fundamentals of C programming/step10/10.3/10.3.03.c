/*

Написать функцию void minmax(int * x, int * y), записывающую в переменную x минимальное из значений x и y, а в переменную y -- максимальное из этих значений.

Sample Input:

15 4

Sample Output:

4 15

*/

void minmax(int * x, int * y){
    int min;
    int max;
    if (*x<*y)
        min = *x;
        max = *y;
    if (*y<*x)
        min = *y;
        max = *x;
    
    *x = min;
    *y = max;
}
