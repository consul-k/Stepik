/*

Измените программу, написанную на прошлом шаге таким образом, чтобы каждое число выводилось столько раз, каково его значение. Например, число 55 должно выводиться 55 раз.

Входные данные:
Два натуральных числа A,B,A,B, таких, что B>A.B>A.

Выходные данные:
AA чисел AA , A+1A+1 чисел A+1A+1 и т.д. Каждое число занимает поле шириной в 4 символа.

Sample Input:

2 5

Sample Output:

2   2   3   3   3   4   4   4   4   5   5   5   5   5

*/

#include <stdio.h>

int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    for (int c=a; c<b+1; c++){
        for (int d=0; d<=c-1; d++){
            printf("%4d",c);}
    }
    return 0;
}
