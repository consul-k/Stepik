/*

Напишите программу считающую произведение цифр заданного kk-значного числа XX.

Входные данные: Два целых числа.
Первое число kk -- количество цифр в числе XX. 1≤k≤41≤k≤4
Второе число XX. Некоторое kk-значное число.

Выходные данные:
Целое число. Произведение цифр числа XX.

Sample Input:

2 48

Sample Output:

32

*/

#include <stdio.h>

int main() {
    int k,    x;
    scanf("%d    %d",   &k,    &x);
    switch(k){
        case    1:    printf("%d\n",    x);    break;
        case    2:    printf("%d\n",    (x/10)*(x%10));    break;
        case    3:    printf("%d\n",    (x/100)*((x/10)%10)*(x%10));    break;
        case    4:    printf("%d\n",    (x/1000)*((x/100)%10)*((x/10)%10)*(x%10));    break;
        default:    printf("ERROR!\n");    break;    
    }
  return 0;
}
