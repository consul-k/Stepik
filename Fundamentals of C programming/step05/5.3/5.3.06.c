/*

Перевод из какой-либо системы счисления с основанием kk в десятичную осуществляется аналогично тому, как вы делали в прошлом задании. Только вместо степеней двойки нужно использовать степени числа kk. Напишите программу для перевода числа из системы счисления с основанием kk в систему счисления с основанием 10.

Входные данные:
Два целых числа. Первое kk - основание системы счисления (2≤k≤82≤k≤8). Второе четырёхразрядное положительное число xx, записанное в kk-ичной системе счисления.

Выходные данные:
Одно целое число, равное числу xx в десятичной системе счисления.

Sample Input:

2 1001

Sample Output:

9

*/

#include <stdio.h>

int main() {
  int k=0,x=0,i=0,res=0;
  scanf("%d%d",&k,&x);
  while(x){
      res = res + x%10*pow(k,i);
      x=x/10;
      i++;
  }
  printf("%d",res);
    
  return 0;
}
