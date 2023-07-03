/*

Минимум-2.
Напишите программу, которая будет вычислять и возвращать минимальное из трёх чисел, переданных в неё, при помощи функции min.

Входные данные:
Три целых числа.

Выходные данные:
Одно целое число -- минимум из чисел, переданных в функцию.

Sample Input:

6 5 7

Sample Output:

5

*/

#include<stdio.h>
int min(int a, int b, int c){
  int min = c;
  if ((a<=c)&&(a<=b)) 
    min = a;
  if ((b<=a)&&(b<=c))
    min = b;
  return min;   
}
int main(void){
    int a=0,b=0,c=0;
    int m = 0;
    
    scanf("%d %d %d",&a,&b,&c);
    m = min(a,b,c);
    
    printf("%d",m);
    
    return 0;
}
